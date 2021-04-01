var getSkyline = function (buildings) {
  let xx = new Set();
  buildings.forEach((b) => {
    xx.add(b[0]);
    xx.add(b[1]);
  });
  let xxx = Array.from(xx.keys()).sort((a, b) => a - b);
  let rtn = [];
  xxx.forEach((x) => {
    let b = buildings.filter((b) => b[0] === x || (b[0] < x && b[1] > x));
    let max = 0;
    for (let i = 0; i < b.length; i++) {
      max = Math.max(max, b[i][2]);
    }
    rtn.push([x, max]);
  });

  for (let i = 1; i < rtn.length; i++) {
    const prv = rtn[i - 1];
    const cur = rtn[i];
    if (prv[1] === cur[1]) {
      rtn.splice(i, 1);
      i--;
    }
  }

  return rtn;
};
