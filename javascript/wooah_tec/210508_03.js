function getDirection(prev, cur) {
  let direction = 0;
  if (prev > cur) {
    direction = -1;
  } else if (prev < cur) {
    direction = 1;
  }
  return direction;
}

function solution(prices) {
  const answer = [];

  let target_price = prices[1]; // 상봉 또는 하봉의 정점의 값
  let before_price = prices[0]; // 직전값

  let backword_width = 1; // 정점으로부터 지나친 길이
  let forward_width = 0; // 정점으로부터 지나친 길이
  // let top_backword_width = 1; // 정점으로부터 지나친 길이
  // let top_forward_width = 1; // 정점으로부터 지나친 길이
  // let bottom_forward_width = 1; // 정점으로부터 지나친 길이
  // let bottom_backword_width = 0; // 정점으로부터 지나간 길이

  //1은 상봉 -2은 하봉 // 0 은 같음

  for (let i = 1; i < prices.length; i++) {
    const price = prices[i];
    const direction = getDirection(prices[i - 1], prices[i]); //1은 상봉 -2은 하봉 // 0 은 같음

    if (i === 1) {
      if (direction !== 0) {
        backword_width += 1;
      }
    } else {
      const beforeDirection = getDirection(prices[i - 2], prices[i - 1]);

      if (beforeDirection === 1) {
        if (direction === 1) {
          backword_width += 1;
        } else if (direction === -1) {
          forwaord_width += 1;
        } else {
          answer.push(
            direction *
              (backword_width < forwaord_width
                ? backword_width
                : forwaord_width)
          );
          backword_width === 0;
          forwaord_width === 0;
        }
      } else if (beforeDirection === -1) {
        if (direction === 1) {
          forwaord_width += 1;
        } else if (direction === -1) {
          backword_width += 1;
        } else {
          answer.push(
            direction *
              (backword_width < forwaord_width
                ? backword_width
                : forwaord_width)
          );
          backword_width === 0;
          forwaord_width === 0;
        }
      } else {
        if (direction) {
          backword_width += 1;
        }
      }
    }
  }
  return answer;
}

console.log(
  // solution([12, 6, 6, 12, 6, 24, 30, 32, 34, 36, 24, 18, 6, 6, 18, 30, 6])
  solution([6, 12, 6])
);
