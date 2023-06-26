const temaOscuro = () => {
    document.querySelector("body").setAttribute("data-bs-theme","dark");
    document.querySelector("#d1-icon").setAttribute("class","bi bi-sun-fill")
    localStorage.setItem("theme", "dark");
}
const temaClaro = () => {
    document.querySelector("body").setAttribute("data-bs-theme","light");
    document.querySelector("#d1-icon").setAttribute("class","bi bi-moon-fill")
    localStorage.setItem("theme", "light");
}
const cambiarTema = () => {
    const storedTheme = localStorage.getItem("theme");
    if (storedTheme === "light") {
        temaOscuro();
      } else {
        temaClaro();
      }
}
window.onload = function () {
    const storedTheme = localStorage.getItem("theme");
  
    // Apply the dark theme if it is stored
    if (storedTheme === "dark") {
      temaOscuro();
    }
};