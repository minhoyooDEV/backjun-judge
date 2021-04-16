function solution(citations) {
  var answer = 0;
  citations.sort((a, b) => b - a);

  const length = citations.length;

  let lowCitation = citations[0];
  for (let i = 0; i < length; i++) {
    const remain_i = length - (i + 1);
    const citation = citations[i];
    lowCitation = Math.min(lowCitation, citation);
    console.log({ remain_i, citation, lowCitation });

    if (citation >= i && citation != 0) {
      answer = Math.min(citation, i + 1);
    } else {
      break;
    }
  }

  return answer;
}

// console.log(solution([3, 0, 6, 1, 5]), 3);
// console.log(solution([4, 0, 6, 1, 5]), 3);
console.log(solution([12, 11, 10, 9, 8, 1]), 5);
console.log(solution([6, 6, 6, 6, 6, 1]), 5);
console.log(solution([4, 4, 4, 5, 0, 1, 2, 3]), 4);
console.log(solution([10, 11, 12, 13]), 4);
console.log(solution([3, 0, 6, 1, 5]), 3);
console.log(solution([0, 0, 1, 1]), 1);
console.log(solution([0, 1]), 1);

function solution2(citations) {
  let answer = 0;
  citations.sort((a, b) => b - a);
  for (let i = 0; i < citations.length; i++) {
    if (citations[i] > i) answer++;
    else break;
  }
  return answer;
}
