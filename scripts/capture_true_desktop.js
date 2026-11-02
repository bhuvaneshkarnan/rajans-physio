const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const http = require('http');

const CHROME = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const ROOT_DIR = path.resolve(__dirname, '..');
const ART_DIR = 'C:\\Users\\bhuva\\.gemini\\antigravity\\brain\\0c98d42e-15a8-45b3-9794-ac6925e26ede';
const PORT = 9224;

async function run() {
  const chromeProc = spawn(CHROME, [
    '--headless=new',
    `--remote-debugging-port=${PORT}`,
    '--no-first-run',
    '--no-default-browser-check'
  ]);

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

  // Desktop Metrics (1280 x 800, DPR 1, mobile: false)
  await send('Emulation.setDeviceMetricsOverride', {
    width: 1280,
    height: 800,
    deviceScaleFactor: 1,
    mobile: false
  });

  const fileUrl = 'file:///' + path.join(ROOT_DIR, 'index.html').replace(/\\/g, '/');
  await send('Page.navigate', { url: fileUrl });

  await new Promise(r => setTimeout(r, 1800));

  const snapDesk = await send('Page.captureScreenshot', { format: 'png' });
  const bufDesk = Buffer.from(snapDesk.data, 'base64');
  const outDesk = path.join(ROOT_DIR, 'true_desktop_hero.png');
  fs.writeFileSync(outDesk, bufDesk);
  fs.writeFileSync(path.join(ART_DIR, 'true_desktop_hero.png'), bufDesk);
  console.log('Saved true_desktop_hero.png (1280x800)');

  ws.close();
  chromeProc.kill();
  process.exit(0);
}

run().catch(err => {
  console.error('Error in Desktop CDP screenshot:', err);
  process.exit(1);
});
