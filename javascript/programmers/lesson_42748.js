const solution = (...a) =>
  a[1].map(([i, j, k]) => a[0].slice(i - 1, j).sort((a, b) => a - b)[k - 1]);

console.log(
  solution(
    [1, 5, 2, 6, 3, 7, 4],
    [
      [2, 5, 3],
      [4, 4, 1],
      [1, 7, 3],
    ]
  )
);