const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const delay = entry.target.getAttribute('data-delay');
        if (delay) {
          entry.target.style.transitionDelay = delay;
        }
        entry.target.classList.add('visible');
      }
    });
  });
  document.querySelectorAll('[data-delay]').forEach(el => observer.observe(el));
  