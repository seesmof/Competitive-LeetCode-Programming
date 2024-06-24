var textContainer = document.querySelector(
  "#__next > div > main > div.w-full.max-w-full > div > div.grid.grid-cols-1.md\\:grid-cols-2.gap-2.mli-auto.w-full.md\\:w-5\\/6.lg\\:w-5\\/6.max-w-\\[1200px\\]"
);
textContainer.classList.remove("md:w-5/6", "lg:w-5/6", "max-w-[1200px]");
textContainer.classList.add("px-4");

var arrowsContainer = document.querySelector(
  "#__next > div > main > div.w-full.max-w-full > div > div.w-\\[90vw\\].flex.sticky.bottom-\\[30\\%\\].z-1.justify-between.max-w-\\[1000px\\].pointer-events-none.mx-auto"
);
arrowsContainer.classList.remove("w-[90vw]", "max-w-[1000px]");
arrowsContainer.classList.add("w-11/12");

var leftArrowLink = document.querySelector(
  "#__next > div > main > div.w-full.max-w-full > div > div.flex.sticky.bottom-\\[30\\%\\].z-1.justify-between.pointer-events-none.mx-auto.w-11\\/12 > div:nth-child(1) > a"
);
var rightArrowLink = document.querySelector(
  "#__next > div > main > div.w-full.max-w-full > div > div.flex.sticky.bottom-\\[30\\%\\].z-1.justify-between.pointer-events-none.mx-auto.w-11\\/12 > div:nth-child(2) > a"
);

document.addEventListener("keydown", function (event) {
  if (event.key === "ArrowLeft") {
    leftArrowLink.click();
  } else if (event.key === "ArrowRight") {
    rightArrowLink.click();
  }
});
