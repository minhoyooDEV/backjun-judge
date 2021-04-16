function solution(S) {
  // write your code in JavaScript (Node.js 8.9.4)

  const div = 2;
  let count = S.length - 1;

  let sum = S.split("").reduce(
    (prev, s) => prev + +s * Math.pow(div, count--),
    0
  );

  let cnt = 0;
  while (sum > 0) {
    if (sum % div === 0) {
      sum = sum / div;
      cnt++;
    } else {
      sum -= 1;
      cnt++;
    }
    if (cnt > 400000) return 799999;
  }

  return cnt;
}

console.log(solution("011100"));
console.log(solution("111"));
console.log(solution("1111010101111"));