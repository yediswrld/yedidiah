// Custom Cursor — only on non-touch/desktop devices
const cursor = document.getElementById('cursor');
const ring = document.getElementById('cursorRing');

const isTouchDevice = () => window.matchMedia('(hover: none) and (pointer: coarse)').matches;

if (cursor && ring) {
  if (isTouchDevice()) {
    cursor.style.display = 'none';
    ring.style.display = 'none';
    document.body.style.cursor = 'auto';
  } else {
    cursor.style.opacity = '0';
    ring.style.opacity = '0';

    document.addEventListener('mousemove', e => {
      cursor.style.opacity = '1';
      ring.style.opacity = '1';
      cursor.style.left = e.clientX + 'px';
      cursor.style.top = e.clientY + 'px';
      setTimeout(() => {
        ring.style.left = e.clientX + 'px';
        ring.style.top = e.clientY + 'px';
      }, 80);
    });

    document.addEventListener('mouseleave', () => {
      cursor.style.opacity = '0';
      ring.style.opacity = '0';
    });

    document.querySelectorAll('a, button').forEach(el => {
      el.addEventListener('mouseenter', () => {
        cursor.style.transform = 'translate(-50%,-50%) scale(2.5)';
        ring.style.transform = 'translate(-50%,-50%) scale(1.5)';
        ring.style.borderColor = 'var(--gold)';
      });
      el.addEventListener('mouseleave', () => {
        cursor.style.transform = 'translate(-50%,-50%) scale(1)';
        ring.style.transform = 'translate(-50%,-50%) scale(1)';
        ring.style.borderColor = 'var(--gold-dim)';
      });
    });
  }
}

// Sticky nav — always visible at top
const nav = document.querySelector('nav');
if (nav) {
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      nav.style.background = 'rgba(8,8,8,0.97)';
      nav.style.borderBottom = '1px solid #222';
    } else {
      nav.style.background = 'linear-gradient(to bottom, rgba(8,8,8,0.95), transparent)';
      nav.style.borderBottom = 'none';
    }
  });
}

// Scroll Reveal
const reveals = document.querySelectorAll('.reveal');
const observer = new IntersectionObserver(entries => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => entry.target.classList.add('visible'), i * 80);
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });
reveals.forEach(el => observer.observe(el));

// Auto-dismiss messages
document.querySelectorAll('.message').forEach(msg => {
  setTimeout(() => msg.style.opacity = '0', 4000);
  setTimeout(() => msg.remove(), 4500);
});