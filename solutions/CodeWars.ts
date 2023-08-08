import { MORSE_CODE } from "./preloaded";
export function decodeMorse(morseCode: string): string {
  let words = morseCode.split("   ");
  const hasSpaces = /^\s*\s*$/g;
  words = words.filter((word) => !hasSpaces.test(word));
  const decodedWords: string[] = [];
  for (let word of words) {
    const letters = word.split(" ");
    for (let i = 0; i < letters.length; i++) {
      const letter = MORSE_CODE[letters[i]];
      if (letter) {
        letters[i] = letter;
      }
    }
    word = letters.join("");
    decodedWords.push(word);
  }
  return decodedWords.join(" ");
}
