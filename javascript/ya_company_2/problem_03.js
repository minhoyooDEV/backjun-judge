function solution(S, T) {
  // write your code in JavaScript (Node.js 8.9.4)
  const sTimes = S.split(":").map(Number);
  const tTimes = T.split(":").map(Number);

  const sSecSum = sTimes[0] * 60 * 60 + sTimes[1] * 60 + sTimes[2];
  const tSecSum = tTimes[0] * 60 * 60 + tTimes[1] * 60 + tTimes[2];

  let [tempHH, tempMM, tempSS] = sTimes;
  let remainSec = tSecSum - sSecSum + 1;
  let count = 0;

  // console.log({ remainSec });

  while (remainSec) {
    const set = new Set();
    [tempHH, tempMM, tempSS].forEach((t) => {
      `${t}`
        .padStart(2, "0")
        .split("")
        .forEach((s) => set.add(s));
    });

    // console.log({ set, size: set.size });

    // console.log({ count, size: set.size, set, result: set.size < 3 }, [
    //   tempHH,
    //   tempMM,
    //   tempSS,
    // ]);

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
  console.log({ count });
  return count;
}

solution("15:15:00", "15:15:12");
solution("22:22:21", "22:22:23");
// solution("22:21:34", "22:22:23");
// solution("15:15:00", "15:16:12");
