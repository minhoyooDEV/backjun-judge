function solution(S) {
  const regx = /[^0-9]/g;
  S = S.replace(regx, "");
  const grouped = [];
  while (S) {
    const len = S.length;
    const cursor = len >= 3 ? 3 : len;
    grouped.push(S.substr(0, cursor));
    S = S.substr(cursor, len);
  }
  const groupedLen = grouped.length;
  const lastEl = grouped[groupedLen - 1];
  if (lastEl.length === 1) {
    const foreheadEl = grouped[groupedLen - 2];
    grouped[groupedLen - 2] = foreheadEl.substr(0, 2);
    grouped[groupedLen - 1] = foreheadEl.substr(2, 1) + grouped[groupedLen - 1];
  }
  return grouped.join("-");
}

//  Driver code to test above method

// console.log(solution("00-44   48 5555 8361"));
console.log(solution("0  -  22 1985--324"));
// console.log(solution([0, 1, 0]));
// console.log(solution([0, 1, 1, 0]));
