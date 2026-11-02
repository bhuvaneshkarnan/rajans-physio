const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const http = require('http');

const CHROME = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const ROOT_DIR = path.resolve(__dirname, '..');
const ART_DIR = 'C:\\Users\\bhuva\\.gemini\\antigravity\\brain\\0c98d42e-15a8-45b3-9794-ac6925e26ede';
const PORT = 9223;

async function run() {
  const chromeProc = spawn(CHROME, [
    '--headless=new',
    `--remote-debugging-port=${PORT}`,
    '--no-first-run',
    '--no-default-browser-check'
  ]);

  // Wait for Chrome to listen
  await new Promise(r => setTimeout(r, 1200));

  function getJson(url) {
    return new Promise((resolve, reject) => {
      http.get(url, res => {
        let data = '';
        res.on('data', chunk => data += chunk);
        res.on('end', () => resolve(JSON.parse(data)));
      }).on('error', reject);
    });
  }

  const list = await getJson(`http://127.0.0.1:${PORT}/json`);
  const page = list.find(p => p.type === 'page') || list[0];
  const wsUrl = page.webSocketDebuggerUrl;

  const ws = new WebSocket(wsUrl);

  let idCounter = 1;
  const pending = new Map();

  function send(method, params = {}) {
    return new Promise((resolve, reject) => {
      const id = idCounter++;
      pending.set(id, { resolve, reject });
      ws.send(JSON.stringify({ id, method, params }));
    });
  }

  ws.onmessage = (event) => {
    const msg = JSON.parse(event.data);
    if (msg.id && pending.has(msg.id)) {
      const { resolve, reject } = pending.get(msg.id);
      pending.delete(msg.id);
      if (msg.error) reject(msg.error);
      else resolve(msg.result);
    }
  };

  await new Promise((resolve) => ws.onopen = resolve);

  await send('Page.enable');
  await send('DOM.enable');

  // Set iPhone 14 Device Metrics (390 x 844, DPR 2, mobile: true)
  await send('Emulation.setDeviceMetricsOverride', {
    width: 390,
    height: 844,
    deviceScaleFactor: 2,
    mobile: true
  });

  const fileUrl = 'file:///' + path.join(ROOT_DIR, 'index.html').replace(/\\/g, '/');
  await send('Page.navigate', { url: fileUrl });

  // Wait for page load
  await new Promise(r => setTimeout(r, 1800));

  // 1. Capture Above-the-Fold Mobile Screen (exact iPhone view)
  const snap1 = await send('Page.captureScreenshot', { format: 'png' });
  const buf1 = Buffer.from(snap1.data, 'base64');
  const out1 = path.join(ROOT_DIR, 'true_iphone_screen.png');
  fs.writeFileSync(out1, buf1);
  fs.writeFileSync(path.join(ART_DIR, 'true_iphone_screen.png'), buf1);
  console.log('Saved true_iphone_screen.png (390x844)');

  // 2. Open Mobile Menu by clicking hamburger button
  const evalClick = await send('Runtime.evaluate', {
    expression: `
      const btn = document.querySelector('.menu-button');
      if (btn) btn.click();
      'clicked';
    `
  });
  await new Promise(r => setTimeout(r, 400));

  // Capture Mobile Menu Open Screen
  const snapMenu = await send('Page.captureScreenshot', { format: 'png' });
  const bufMenu = Buffer.from(snapMenu.data, 'base64');
  const outMenu = path.join(ROOT_DIR, 'true_iphone_menu_open.png');
  fs.writeFileSync(outMenu, bufMenu);
  fs.writeFileSync(path.join(ART_DIR, 'true_iphone_menu_open.png'), bufMenu);
  console.log('Saved true_iphone_menu_open.png');

  ws.close();
  chromeProc.kill();
  process.exit(0);
}

run().catch(err => {
  console.error('Error in CDP screenshot:', err);
  process.exit(1);
});
