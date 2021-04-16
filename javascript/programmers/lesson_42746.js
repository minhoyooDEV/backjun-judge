function solution(numbers) {
  const s = numbers
    .map(String)
    .sort((a, b) => b + a - (a + b))
    .join("");
  return s[0] === "0" ? "0" : s;
}

console.log(solution([6, 10, 2]));
console.log(solution([3, 31, 32, 30, 34, 5, 9]));
console.log(solution([0, 0, 0]));
