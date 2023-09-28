export function findMissingLetter(array: string[]): string {
  const alphabet = "abcdefghijklmnopqrstuvwxyz";
  const alphabetUpper = alphabet.toUpperCase();
  // get an index of the first letter in the alphabet array
  const index = alphabet.indexOf(array[0]);
  // iterate through the given array and check if the current letter is in the alphabet
  for (let i = 1; i <= array.length; i++) {
    if (array[i] === array[i].toLowerCase()) {
      if (array[i] !== alphabet[index]) {
        return alphabet[index];
      }
    } else if (array[i] === array[i].toUpperCase()) {
      if (array[i] !== alphabetUpper[index]) {
        return alphabetUpper[index];
      }
    }
  }

  return "";
}
