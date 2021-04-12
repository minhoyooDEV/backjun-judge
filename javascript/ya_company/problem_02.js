function func(A = []) {
  const map = new Map();
  let indices = [];

  let sum = 0;
  let subArraysCount = 0;

  for (let i = 0; i < A.length; i++) {
    const n = A[i];
    sum += n;

    if (sum == 0) subArraysCount++;
    indices = [];

    if (map.get(sum)) {
      subArraysCount += map.get(sum).length;
      indices = map.get(sum);
    }

    indices.push(i);
    map.set(sum, indices);
    if (subArraysCount > 1000000000) {
      console.log(subArraysCount);
      return -1;
    }
  }
  return subArraysCount;
}

console.log(func([2, -2, 3, 0, 4, -7]));
console.log(func(Array(100000).fill(0)));
console.log(func(Array(4).fill(0)));
console.log(func(Array(447110).fill(0)));
