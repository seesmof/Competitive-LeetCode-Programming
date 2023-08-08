export function getSum(a: number, b: number): number {
  // Good luck!
  if (a === b) return a;
  let sum: number = 0;
  for (let i = Math.min(a, b); i <= Math.max(a, b); i++) {
    sum += i;
  }
  return sum;
}
