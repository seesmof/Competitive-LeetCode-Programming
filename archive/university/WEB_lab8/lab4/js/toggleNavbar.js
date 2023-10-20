// toggleNavbar.js task 2

document
  .querySelector("#navbar-toggle-button")
  .addEventListener("click", () => {
    document.querySelector(".navbar").classList.toggle("hidden");
    console.log("button clicked");
  });
