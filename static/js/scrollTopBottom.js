// Functionality for Results page Scroll Buttons
const topButton = document.querySelector(".top_button");
topButton.onclick = () => window.scrollTo({ top: 0, behavior: "smooth" });

const bottomButton = document.querySelector(".bottom_button");
bottomButton.onclick = () => window.scrollTo({ top: 10000, behavior: "smooth" });