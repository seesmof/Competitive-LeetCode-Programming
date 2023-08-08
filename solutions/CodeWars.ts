export function isValidWalk(walk: string[]) {
  if (walk.length !== 10) return false;
  let distanceFromStart = 0;
  const calculateDistanceFromStart = ({
    currentPosition,
  }: {
    currentPosition: number;
  }) => {};

  for (let i = 0; i < walk.length; i++) {
    if (walk[i] === "n") {
      distanceFromStart--;
    } else if (walk[i] === "s") {
      distanceFromStart++;
    }
  }
  return distanceFromStart === 0;
}
