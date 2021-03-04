// N개의 마을로 이루어진 나라가 있습니다. 이 나라의 각 마을에는 1부터 N까지의 번호가 각각 하나씩 부여되어 있습니다. 각 마을은 양방향으로 통행할 수 있는 도로로 연결되어 있는데, 서로 다른 마을 간에 이동할 때는 이 도로를 지나야 합니다. 도로를 지날 때 걸리는 시간은 도로별로 다릅니다. 현재 1번 마을에 있는 음식점에서 각 마을로 음식 배달을 하려고 합니다. 각 마을로부터 음식 주문을 받으려고 하는데, N개의 마을 중에서 K 시간 이하로 배달이 가능한 마을에서만 주문을 받으려고 합니다. 다음은 N = 5, K = 3인 경우의 예시입니다.

function solution(N, road, K) {
  const map = {};
  const distances = {};
  for (let i = 1; i <= N; i++) {
    map[i] = [];
    distances[i] = Infinity;
  }
  console.log(map);
  for (const r of road) {
    const [a, b, c] = r;
    map[a].push([b, c]);
    map[b].push([a, c]);
  }

  distances[1] = 0;
  const queue = [];

  queue.push([1, distances[1]]);
  while (queue.length) {
    const [currentNode, currentDistance] = queue.shift();
    if (distances[currentNode] < currentDistance) {
      continue;
    }

    for (const besideNode of map[currentNode]) {
      const [nextNode, distance] = besideNode;
      const calcedDistance = currentDistance + distance;
      if (calcedDistance < distances[nextNode]) {
        distances[nextNode] = calcedDistance;
        queue.push([nextNode, distances[nextNode]]);
      }
    }
    queue.sort(([, aD], [, bD]) => bD - aD);
  }

  return Object.values(distances).filter((v) => v <= K).length;
}

// Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

// Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

function solution2(brown, yellow) {
  const sum = brown + yellow;
  for (let i = 3; i <= sum; i++) {
    // 약수를 구하는 부분
    if (sum % i === 0) {
      const w = i;
      const h = Number(sum / i);
      if ((w - 2) * (h - 2) === yellow) {
        return w < h ? [h, w] : [w, h];
      }
    }
  }
  return [0, 0];
}