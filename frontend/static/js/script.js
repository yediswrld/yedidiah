/* Add these to your existing style.css — update the nav section */

/* Make nav fully sticky */
nav {
  position: fixed; top: 0; left: 0; right: 0;
  z-index: 100; padding: 24px 60px;
  display: flex; justify-content: space-between; align-items: center;
  background: linear-gradient(to bottom, rgba(8,8,8,0.95), transparent);
  transition: background 0.3s, border-bottom 0.3s;
}

/* Hide custom cursor on touch devices */
@media (hover: none) and (pointer: coarse) {
  .cursor, .cursor-ring { display: none !important; }
  body { cursor: auto !important; }
}