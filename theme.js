document.addEventListener('DOMContentLoaded', function() {
  const themeToggle = document.getElementById('theme-toggle');
  const body = document.body;

  function setIcon() {
    if (body.classList.contains('dark')) {
      themeToggle.textContent = '☀️'; // Sun in dark mode
    } else {
      themeToggle.textContent = '🌙'; // Moon in light mode
    }
  }

  themeToggle.addEventListener('click', function() {
    body.classList.toggle('dark');
    setIcon();
    // Optionally, persist theme in localStorage
    if (body.classList.contains('dark')) {
      localStorage.setItem('theme', 'dark');
    } else {
      localStorage.setItem('theme', 'light');
    }
  });

  // On load, set theme from localStorage
  if (localStorage.getItem('theme') === 'dark') {
    body.classList.add('dark');
  } else {
    body.classList.remove('dark');
  }
  setIcon();
}); 