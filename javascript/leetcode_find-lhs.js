var findLHS = function (nums) {
  const data = {};
  nums.forEach((n) => {
    if (data[n]) {
      data[n] += 1;
    } else {
      data[n] = 1;
    }
  });

  let maxLen = 0;
  for (const key of Object.keys(data)) {
    const mn = +key - 1;
    const mx = +key + 1;

    if (maxLen < data[mn] + data[key]) {
      maxLen = data[mn] + data[key];
    }
    if (maxLen <= data[mx] + data[key]) {
      maxLen = data[mx] + data[key];
    }
  }

  return maxLen;
};

var bestFindLHS = function(nums) {
  const map = new Map()
  let max = 0

  for(const num of nums){
      map.set(num, map.get(num) + 1 || 1)
  }

  for(const num of nums){
      if(map.has(num + 1)) {
          max = Math.max(max, map.get(num) + map.get(num + 1))
      }
  }

  return max
};



console.log(findLHS([1, 2, 3, 4]));
console.log(findLHS([1,3,2,2,5,2,3,7]));
