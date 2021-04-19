function solution(S, T) {
  // write your code in JavaScript (Node.js 8.9.4)
  const sTimes = S.split(':').map(Number);
  const tTimes = T.split(':').map(Number);

  // before & after
  const sSecSum = sTimes[0] * 60 * 60 + sTimes[1] * 60 + sTimes[2];
  const tSecSum = tTimes.reduce((prev, t, i) => prev + t * Math.pow(60, tTimes.length - i - 1), 0);

  let [tempHH, tempMM, tempSS] = sTimes;
  let remainSec = tSecSum - sSecSum + 1;
  let count = 0;

  while (remainSec) {
    const set = new Set();
    [tempHH, tempMM, tempSS].forEach((t) => {
      // after
      if (t < 10) {
        set.add(0);
        set.add(t);
      } else {
        set.add(parseInt(t / 10));
        set.add(t % 10);
      }
      // before
      // `${t}`
      //   .padStart(2, '0')
      //   .split('')
      //   .forEach((s) => set.add(s));
    });

    remainSec--;

    tempSS += 1;
    if (!(tempSS % 60)) {
      tempSS = 0;
      tempMM += 1;

      if (!(tempMM % 60)) {
        tempMM = 0;
        tempHH += 1;
        if (!(tempHH % 24)) {
          tempHH = 0;
        }
      }
    }

    if (set.size < 3) {
      count += 1;
    }
  }
  return count;
}

console.log(solution('15:15:00', '15:15:12'), 1);
console.log(solution('22:22:21', '22:22:23'), 3);
console.log(solution('22:21:34', '22:22:23'), 8);
console.log(solution('15:15:00', '15:16:12'), 4);
