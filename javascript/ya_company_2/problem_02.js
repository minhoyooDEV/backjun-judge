// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(ranks) {
  // write your code in JavaScript (Node.js 8.9.4)

  ranks.sort();

  const countMap = new Map();

  for (const rank of ranks) {
    countMap.set(rank, (countMap.get(rank) || 0) + 1);
  }

  let sum = 0;
  countMap.forEach((_, soldierKey) => {
    const superiorKey = soldierKey + 1;
    const value = countMap.get(superiorKey);
    if (value) {
      sum += countMap.get(soldierKey);
    }
  });

  return sum;
}



console.time('t1')
console.log(solution([0,5,0,2,4,3,2]), 4)
console.timeEnd('t1')