// Bouton clair/sombre : bascule data-theme et mémorise le choix
document.addEventListener('DOMContentLoaded', function () {
  var btn = document.getElementById('theme-toggle')
  if (!btn) return

  function label() {
    var dark = document.documentElement.dataset.theme === 'dark'
    btn.setAttribute('aria-label', dark ? 'Passer en mode clair' : 'Passer en mode sombre')
    btn.setAttribute('title', btn.getAttribute('aria-label'))
  }

  label()
  btn.addEventListener('click', function () {
    var next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark'
    document.documentElement.dataset.theme = next
    try { localStorage.setItem('rh-theme', next) } catch (e) {}
    label()
  })
})
