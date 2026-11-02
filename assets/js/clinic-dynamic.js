/**
 * Rajan's Physiotherapy & Pain Relief Centre
 * Comprehensive Dynamic UI, Smooth Scroll & End-to-End Animations Suite
 * Designed with 60fps Native Performance, Mobile Optimization & Zero Shadows
 */

(function () {
  'use strict';

  var SVG_WHATSAPP = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="flex-shrink:0;"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19.01L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.67 12.05 3.67M9.53 7.32C9.36 7.32 9.09 7.38 8.86 7.63C8.63 7.88 7.98 8.49 7.98 9.73C7.98 10.97 8.88 12.17 9.01 12.34C9.14 12.51 10.77 15.02 13.27 16.1C13.86 16.36 14.33 16.51 14.68 16.62C15.28 16.82 15.82 16.79 16.26 16.72C16.75 16.65 17.76 16.11 17.97 15.52C18.18 14.93 18.18 14.43 18.11 14.32C18.05 14.21 17.88 14.15 17.62 14.02C17.37 13.89 16.13 13.28 15.9 13.2C15.68 13.11 15.51 13.07 15.34 13.32C15.17 13.57 14.69 14.15 14.55 14.32C14.4 14.48 14.26 14.51 14.01 14.38C13.75 14.25 12.93 13.99 11.96 13.12C11.2 12.44 10.69 11.61 10.54 11.36C10.4 11.11 10.53 10.97 10.66 10.84C10.77 10.73 10.91 10.54 11.05 10.38C11.19 10.21 11.23 10.09 11.32 9.92C11.41 9.75 11.36 9.61 11.3 9.48C11.23 9.36 10.72 8.1 10.51 7.59C10.3 7.09 10.09 7.16 9.93 7.15C9.79 7.14 9.62 7.32 9.53 7.32Z"/></svg>';

  // 1. Inject UI Overlays (Scroll Progress, Floating WhatsApp, Back to Top)
  function injectUIElements() {
    // Scroll progress bar
    if (!document.getElementById('scroll-progress')) {
      var progress = document.createElement('div');
      progress.id = 'scroll-progress';
      document.body.prepend(progress);
    }

    // Floating Back to Top button
    if (!document.getElementById('back-to-top')) {
      var btt = document.createElement('button');
      btt.id = 'back-to-top';
      btt.setAttribute('aria-label', 'Back to top');
      btt.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>';
      document.body.appendChild(btt);

      btt.addEventListener('click', function () {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }

    // Floating WhatsApp Button (Zero Shadows, Clean Flat Design)
    if (!document.getElementById('floating-whatsapp')) {
      var waBtn = document.createElement('a');
      waBtn.id = 'floating-whatsapp';
      waBtn.href = 'https://wa.me/919042612895?text=Hello%20Dr.%20Prabhu%2C%20I%20would%20like%20to%20consult%20regarding%20physiotherapy';
      waBtn.target = '_blank';
      waBtn.rel = 'noopener';
      waBtn.setAttribute('aria-label', 'Chat on WhatsApp with Dr. Prabhu Rajan');
      waBtn.innerHTML = SVG_WHATSAPP + '<span>WhatsApp Consultation</span>';
      document.body.appendChild(waBtn);
    }
  }

  // 2. Scroll Progress & Sticky Navbar Handler
  function setupScrollTracking() {
    var progressBar = document.getElementById('scroll-progress');
    var btt = document.getElementById('back-to-top');
    var waBtn = document.getElementById('floating-whatsapp');
    var navbar = document.querySelector('.navbar');

    function onScroll() {
      var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      var docHeight = document.documentElement.scrollHeight - window.innerHeight;
      var scrollPercent = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;

      if (progressBar) {
        progressBar.style.width = scrollPercent + '%';
      }

      if (navbar) {
        if (scrollTop > 40) {
          navbar.classList.add('scrolled');
        } else {
          navbar.classList.remove('scrolled');
        }
      }

      if (btt) {
        if (scrollTop > 380) {
          btt.classList.add('visible');
        } else {
          btt.classList.remove('visible');
        }
      }

      if (waBtn) {
        if (scrollTop > 120) {
          waBtn.style.opacity = '1';
          waBtn.style.pointerEvents = 'auto';
        } else {
          waBtn.style.opacity = '0.9';
        }
      }
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // 3. Number Counter Animation with Cubic Easing
  function animateCounter(el) {
    if (el.dataset.animated === 'true') return;
    el.dataset.animated = 'true';

    var rawValue = el.getAttribute('data-counter') || el.innerText;
    var target = parseFloat(rawValue.replace(/[^0-9.]/g, ''));
    if (isNaN(target)) return;

    var isDecimal = target % 1 !== 0;
    var prefix = el.getAttribute('data-prefix') || '';
    var suffix = el.getAttribute('data-suffix') || '';

    if (!suffix) {
      var raw = el.innerText.trim();
      if (raw.endsWith('+')) suffix = '+';
      else if (raw.endsWith('%')) suffix = '%';
    }

    var duration = 2200; // ms
    var startTime = null;

    function step(timestamp) {
      if (!startTime) startTime = timestamp;
      var elapsed = timestamp - startTime;
      var progress = Math.min(elapsed / duration, 1);

      // Smooth ease-out cubic curve
      var easeOut = 1 - Math.pow(1 - progress, 3);
      var current = target * easeOut;

      if (isDecimal) {
        el.innerText = prefix + current.toFixed(1) + suffix;
      } else {
        var rounded = Math.floor(current);
        el.innerText = prefix + rounded.toLocaleString() + suffix;
      }

      if (progress < 1) {
        requestAnimationFrame(step);
      } else {
        if (isDecimal) {
          el.innerText = prefix + target.toFixed(1) + suffix;
        } else {
          el.innerText = prefix + Math.floor(target).toLocaleString() + suffix;
        }
      }
    }

    requestAnimationFrame(step);
  }

  // 4. End-to-End Blurred Reveal Scroll Animations
  function setupScrollReveals() {
    // Automatically attach reveal-blur to key interactive cards across every page
    var candidateSelectors = [
      '.service-card',
      '.bento-card',
      '.photo-card',
      '.testimonial-card',
      '.pricing-card',
      '.vs-card',
      '.process-step',
      '.faq-item'
    ];

    document.querySelectorAll(candidateSelectors.join(',')).forEach(function (card, index) {
      if (!card.classList.contains('reveal-blur')) {
        card.classList.add('reveal-blur');
        if (!card.classList.contains('stagger-1') && !card.classList.contains('stagger-2') && !card.classList.contains('stagger-3')) {
          var staggerIdx = (index % 6) + 1;
          card.classList.add('stagger-' + staggerIdx);
        }
      }
    });

    // Reveal hero elements immediately so above-the-fold content is instantly sharp
    document.querySelectorAll('.section--hero .reveal-blur, header .reveal-blur, .section--hero [data-counter]').forEach(function (el) {
      el.classList.add('revealed');
    });

    // Start hero counters after slight pause
    setTimeout(function () {
      document.querySelectorAll('.section--hero [data-counter]').forEach(animateCounter);
    }, 280);

    // Setup IntersectionObserver
    if (!('IntersectionObserver' in window)) {
      document.querySelectorAll('.reveal-blur').forEach(function (el) {
        el.classList.add('revealed');
      });
      document.querySelectorAll('[data-counter]').forEach(animateCounter);
      return;
    }

    var observer = new IntersectionObserver(
      function (entries, obs) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('revealed');

            // Trigger internal counters
            setTimeout(function () {
              entry.target.querySelectorAll('[data-counter]').forEach(animateCounter);
              if (entry.target.hasAttribute('data-counter')) {
                animateCounter(entry.target);
              }
            }, 180);

            obs.unobserve(entry.target);
          }
        });
      },
      {
        root: null,
        rootMargin: '0px 0px -40px 0px',
        threshold: 0.12
      }
    );

    document.querySelectorAll('.reveal-blur').forEach(function (el) {
      observer.observe(el);
    });

    document.querySelectorAll('[data-counter]').forEach(function (el) {
      if (!el.closest('.reveal-blur') && !el.closest('.section--hero')) {
        observer.observe(el);
      }
    });
  }

  // 5. Smooth Momentum Inertia Scrolling (Cinematic Desktop Damping)
  function setupSmoothMomentumScroll() {
    // Keep native 120Hz momentum on touch screens (phones / tablets)
    if ('ontouchstart' in window || navigator.maxTouchPoints > 0) return;

    var currentY = window.pageYOffset || document.documentElement.scrollTop;
    var targetY = currentY;
    var isRunning = false;
    var lerpFactor = 0.082; // Silky smooth damping factor

    window.addEventListener('wheel', function (e) {
      // Don't intercept inside input fields, textareas, or modal dropdowns
      if (e.target.closest('textarea, select, input, .w-dropdown-list')) return;

      var maxScroll = Math.max(0, document.documentElement.scrollHeight - window.innerHeight);
      if (maxScroll <= 0) return;

      e.preventDefault();
      targetY += e.deltaY * 0.88;
      targetY = Math.max(0, Math.min(maxScroll, targetY));

      if (!isRunning) {
        isRunning = true;
        requestAnimationFrame(renderScroll);
      }
    }, { passive: false });

    function renderScroll() {
      var diff = targetY - currentY;
      if (Math.abs(diff) > 0.4) {
        currentY += diff * lerpFactor;
        window.scrollTo(0, currentY);
        requestAnimationFrame(renderScroll);
      } else {
        currentY = targetY;
        window.scrollTo(0, currentY);
        isRunning = false;
      }
    }

    window.addEventListener('scroll', function () {
      if (!isRunning) {
        currentY = window.pageYOffset || document.documentElement.scrollTop;
        targetY = currentY;
      }
    }, { passive: true });
  }

  // 6. Interactive FAQ Accordion Transitions
  function setupFAQAccordions() {
    var faqItems = document.querySelectorAll('.faq-item');
    if (!faqItems.length) return;

    faqItems.forEach(function (item) {
      var q = item.querySelector('.faq-q');
      if (!q) return;

      if (!q.querySelector('.faq-icon')) {
        var icon = document.createElement('span');
        icon.className = 'faq-icon';
        icon.innerHTML = '+';
        q.appendChild(icon);
      }

      q.addEventListener('click', function () {
        var isOpen = item.classList.contains('active');

        // Close sibling accordions in same group
        var parent = item.parentElement;
        if (parent) {
          parent.querySelectorAll('.faq-item.active').forEach(function (activeItem) {
            if (activeItem !== item) {
              activeItem.classList.remove('active');
            }
          });
        }

        if (isOpen) {
          item.classList.remove('active');
        } else {
          item.classList.add('active');
        }
      });
    });
  }

  // 7. Smooth Scroll for Anchor Links
  function setupSmoothAnchors() {
    document.addEventListener('click', function (e) {
      var link = e.target.closest('a[href^="#"], a[href^="/#"]');
      if (!link) return;

      var href = link.getAttribute('href');
      var hash = href.includes('#') ? '#' + href.split('#')[1] : '';
      if (!hash || hash === '#') return;

      var target = document.querySelector(hash);
      if (target) {
        e.preventDefault();
        var navHeight = 72;
        var top = target.getBoundingClientRect().top + window.pageYOffset - navHeight;
        window.scrollTo({ top: Math.max(0, top), behavior: 'smooth' });
      }
    });
  }


  // 7. Mobile Navigation Drawer Toggle Handler
  function setupMobileNav() {
    var menuButtons = document.querySelectorAll('.menu-button, .w-nav-button');
    var navMenus = document.querySelectorAll('.nav-menu, .w-nav-menu');

    menuButtons.forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        var isOpen = btn.classList.contains('open') || btn.classList.contains('w--open');
        
        if (isOpen) {
          btn.classList.remove('open', 'w--open');
          navMenus.forEach(function (m) { m.classList.remove('open', 'w--nav-menu-open'); });
          document.body.classList.remove('nav-menu-open');
        } else {
          btn.classList.add('open', 'w--open');
          navMenus.forEach(function (m) { m.classList.add('open', 'w--nav-menu-open'); });
          document.body.classList.add('nav-menu-open');
        }
      });
    });

    // Close mobile nav when clicking any regular nav link
    document.querySelectorAll('.nav-menu a:not(.w-dropdown-toggle), .w-nav-menu a:not(.w-dropdown-toggle)').forEach(function (link) {
      link.addEventListener('click', function () {
        menuButtons.forEach(function (b) { b.classList.remove('open', 'w--open'); });
        navMenus.forEach(function (m) { m.classList.remove('open', 'w--nav-menu-open'); });
        document.body.classList.remove('nav-menu-open');
      });
    });

    // Mobile dropdown accordion for Services
    document.querySelectorAll('.nav-menu .w-dropdown-toggle, .w-nav-menu .w-dropdown-toggle').forEach(function (toggle) {
      toggle.addEventListener('click', function (e) {
        if (window.innerWidth <= 991) {
          e.preventDefault();
          e.stopPropagation();
          var list = this.parentElement ? this.parentElement.querySelector('.w-dropdown-list') : null;
          if (list) {
            var isShown = list.classList.contains('open') || list.classList.contains('w--open');
            list.classList.toggle('open', !isShown);
            list.classList.toggle('w--open', !isShown);
            list.style.display = isShown ? 'none' : 'block';
          }
        }
      });
    });

    // Close when clicking outside navbar
    document.addEventListener('click', function (e) {
      if (!e.target.closest('.navbar') && document.body.classList.contains('nav-menu-open')) {
        menuButtons.forEach(function (b) { b.classList.remove('open', 'w--open'); });
        navMenus.forEach(function (m) { m.classList.remove('open', 'w--nav-menu-open'); });
        document.body.classList.remove('nav-menu-open');
      }
    });
  }

  // 8. Initialize on DOM Ready
  function init() {
    injectUIElements();
    setupScrollTracking();
    setupScrollReveals();
    setupSmoothMomentumScroll();
    setupFAQAccordions();
    setupSmoothAnchors();
    setupMobileNav();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
