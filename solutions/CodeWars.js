function getMiddle(s) {
  //Code goes here!
  if (s.length % 2 === 0) {
    return s[Math.floor(s.length / 2) - 1] + s[Math.ceil(s.length / 2)];
  }
  return s[Math.floor(s.length / 2)];
}

console.log(getMiddle("hello"));
console.log(getMiddle("test"));
