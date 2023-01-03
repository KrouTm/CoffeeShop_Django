///Navbar
const Mobile = document.getElementById('mobile');
Mobile.addEventListener('click', toggleMenu);
Mobile.addEventListener('touchstart', toggleMenu);

function toggleMenu(event) {
    if (event.type === 'touchstart') event.preventDefault();
    const nav = document.getElementById('nav');
    nav.classList.toggle('active');
    const active = nav.classList.contains('active');
    event.currentTarget.setAttribute('aria-expanded', active);
    if (active) {event.currentTarget.setAttribute('aria-label', 'Close menu');}
    else {event.currentTarget.setAttribute('aria-label', 'Open menu');}
}