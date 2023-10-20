// randomQuotes.js task 3

const quotes = [
  "The only way to do great work is to love what you do.",
  "Believe you can and you're halfway there.",
  "Don't watch the clock; do what it does. Keep going.",
  "The harder you work for something, the greater you'll feel when you achieve it.",
  "Dream it. Believe it. Build it.",
];

const randomQuote = () => {
  const index = Math.floor(Math.random() * quotes.length);
  return quotes[index];
};

export { randomQuote };
