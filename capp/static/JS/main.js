/* CURSOR */
const cursor = document.querySelector(".cursor");
const EXPAND_TIMEOUT = 500;

document.addEventListener("mousemove", (e) => {
  cursor.style.top = e.pageY - window.scrollY - 10 + "px";
  cursor.style.left = e.pageX - window.scrollX - 10 + "px";
});

document.addEventListener("click", (e) => {
  cursor.classList.add("expand");
  setTimeout(() => {
    cursor.classList.remove("expand");
  }, EXPAND_TIMEOUT);
});
