const quotes = [
  "Don't cry because it's over, smile because it happened.",
  "The greatest glory in living lies not in never falling, but in rising every time we fall.",
  "The way to get started is to quit talking and begin doing.",
  "Remember that not getting what you want is sometimes a wonderful stroke of luck.",
  "If you tell the truth, you don't have to remember anything.",
  "You only live once, but if you do it right, once is enough.",
  "In the end, it's not the years in your life that count. It's the life in your years.",
  "Be the change that you wish to see in the world.",
];

const randomQuote = () => {
  const index = Math.floor(Math.random() * quotes.length);
  return quotes[index];
};

export { randomQuote };
