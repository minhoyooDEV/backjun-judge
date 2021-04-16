function solution(S) {
  const div = 2;
  let count = S.length - 1;

  let sum = S.split('').reduce((prev, s) => prev + +s * Math.pow(div, count--), 0);

  let cnt = 0;
  while (sum > 0) {
    // console.log(sum)
    if (sum % div === 0) {
      sum = sum / div;
      cnt++;
    } else {
      sum -= 1;
      cnt++;
    }
    if (cnt > 400000) return 799999;
  }
  // console.timeEnd('Sum #2');

  return cnt;
}

// console.log(solution('011100'), 7);
// console.log(solution('111'), 5);
// console.log(solution("1111010101111"), 22);

/**
 * @param {string} s
 */
const solution2 = (s) => {
  let answer = 0;
  const ary = s.split('');

  while (true) {
    const lastIdx = ary.length - 1;
    const lastOneIdx = ary.lastIndexOf('1');
    // console.log( parseInt(ary.join(''), 2))
    if (lastOneIdx === -1) {
      return answer;
    }
    answer += 1;
    // console.log({lastOneIdx , lastIdx})
    if (lastOneIdx === lastIdx) {
      ary[lastIdx] = '0';
    } else {
      ary.pop();
    }
  }

  return a;
};

// console.log(solution2('011100'), 7);
// console.log(solution2('111'), 5);
// console.log(solution2('1111010101111'), 5);

// const a0 = new Date();
// console.log(solution('111101010111111110101001001011111111'), 22);
// const a1 = new Date();
// const b0 = new Date();
// console.log(solution2('111101010111111110101001001011111111'), 22);
// const b1 = new Date();

['111101010111100100101111111111110101011111111010100'].forEach((s) => {

  const div = 2;
  let count = s.length - 1;

  // console.time('Sum #1');
  let sum = s.split('').reduce((prev, S) => prev + +S * Math.pow(div, count--), 0);
  console.log('@@@@ start number: ' + parseInt(s, 2), 'sum: ' + sum)
  const a0 = new Date();
  const r0 = solution2(s);
  const a1 = new Date();
  const b0 = new Date();
  const r1 = solution(s);
  const b1 = new Date();
  console.log(r0, r1, r0 === r1);
  console.log(a1.getTime() - a0.getTime(), b1.getTime() - b0.getTime(), a1.getTime() - a0.getTime() > b1.getTime() - b0.getTime());
});



