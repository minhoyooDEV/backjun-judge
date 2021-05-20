function func(list, cursor) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] != cursor) {
      count++;
    }
    cursor = cursor === 0 ? 1 : 0;
  }

  return count;
}
function solution(A) {
  return Math.min(func(A, 0), func(A, 1));
}

//  Driver code to test above method

console.log(solution([1, 0, 1, 0, 1, 1]));
console.log(solution([1, 1, 0, 1, 1]));
console.log(solution([0, 1, 0]));
console.log(solution([0, 1, 1, 0]));
