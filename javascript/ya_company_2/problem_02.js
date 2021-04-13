// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(ranks) {
  // write your code in JavaScript (Node.js 8.9.4)

  ranks.sort();

  const countMap = new Map();

  for (const rank of ranks) {
    countMap.set(rank, (countMap.get(rank) || 0) + 1);
  }
  // console.log(ranks);
  // console.log(countMap);

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

// console.log(solution([3, 4, 3, 0, 2, 2, 3, 0, 0]));

//
// int sum = 0;
//         Arrays.sort(ranks);

//         Map<Integer, Integer> count = new HashMap<>();
//         for(Integer rank:ranks){
//             count.put(rank, count.getOrDefault(rank, 0)+1);
//         }

//         for(Integer key:count.keySet()){
//             Integer highKey = key+1;
//             if(count.get(highKey)!=null){
//                 sum+=count.get(key);
//             }
//         }
//         return sum;
