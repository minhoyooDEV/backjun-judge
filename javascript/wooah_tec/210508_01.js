function solution(weights, head2head) {
  const length = weights.length;

  const winCnt = {};
  const heavyWeightWinCnt = {};
  for (let i = 0; i < length; i++) {
    winCnt[i] = 0;
    heavyWeightWinCnt[i] = 0;
  }

  const weightsdict = weights.reduce(
    (prev, value, i) => ({ ...prev, [i]: value }),
    {}
  );

  const weightsort = Object.entries(weightsdict).sort((a, b) => b[1] - a[1]);

  const weightidx = weightsort.map((value) => +value[0]);

  // console.log({ winCnt, weightsdict, weightsort, weightidx });
  for (let idx = 0; idx < head2head.length; idx++) {
    const vs = head2head[idx];
    for (let i = 0; i < length; i++) {
      if (vs[i] === "W") {
        winCnt[idx] += 1;
        if (weights[idx] < weights[i]) {
          heavyWeightWinCnt[idx] += 1;
        }
      }
    }
  }
  //   weightsdict {0: 60, 1: 70, 2: 60}
  // weightsort [(1, 70), (0, 60), (2, 60)]
  // weightidx [1, 0, 2]
  // weightidx [1, 0, 2]
  // heavyWeightdict {1: 0, 0: 0, 2: 0}
  // heavyWeightSort [(1, 0), (0, 0), (2, 0)]
  // heavyWeightidx [1, 0, 2]
  // winCntdict {1: 0, 0: 0, 2: 0}
  // winCntSort [(1, 0), (0, 0), (2, 0)]
  // winCntidx [1, 0, 2]

  const heavyWeightdict = {};
  for (const i in weightidx) {
    heavyWeightdict[i] = heavyWeightWinCnt[i];
  }

  const heavyWeightSort = Object.entries(heavyWeightdict).sort(
    (a, b) => b[1] - a[1]
  );
  const heavyWeightidx = heavyWeightSort.map((v) => v[0]);

  const winCntdict = {};
  const winCntDict2 = new Map();
  for (const value of heavyWeightidx) {
    // console.log({ value });
    winCntDict2[value] = winCnt[value];
    // winCntdict[value] = winCnt[value];
    winCntDict2.set(value, winCnt[value]);
  }

  console.log([...winCntDict2]);
  // const winCntSort = Object.entries(winCntdict).sort((a, b) => b[1] - a[1]);
  const winCntSort2 = [...winCntDict2].sort((a, b) => b[1] - a[1]);

  const winCntIdx = winCntSort2.map((v) => +v[0] + 1);

  console.log({
    heavyWeightWinCnt,
    heavyWeightdict,
    heavyWeightSort,
    heavyWeightidx,
    winCntdict,
    winCntDict2,
  });
  console.log({ winCntSort2 });
  console.log({
    //   heavyWeightSort,
    //   winCntdict,
    //   winCntSort,
    //   winCntIdx,
  });

  // weightsdict {0: 60, 1: 70, 2: 60}
  // weightsort [(1, 70), (0, 60), (2, 60)]
  // weightidx [1, 0, 2]
  // heavyWeightWinCnt defaultdict(<class 'int'>, {1: 0, 0: 0, 2: 0})
  // heavyWeightdict {1: 0, 0: 0, 2: 0}
  // heavyWeightSort [(1, 0), (0, 0), (2, 0)]
  // heavyWeightidx [1, 0, 2]
  // winCntdict {1: 0, 0: 0, 2: 0}
  // winCntSort [(1, 0), (0, 0), (2, 0)]
  // winCntidx [1, 0, 2]
  // [2, 1, 3]

  return winCntIdx;
}

// console.log(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]));
console.log(solution([145, 92, 86], ["NLW", "WNL", "LWN"]));
