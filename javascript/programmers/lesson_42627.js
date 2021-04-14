function solution(jobs) {
  jobs.sort((a, b) => a[0] - b[0] || a[1] - b[1]);

  const tasks = [...jobs];
  const queue = [];
  queue.push(tasks.shift());
  queue.sort((a, b) => a[1] - b[1]);

  let currentTime = 0,
    totalResponseTime = 0;
  while (queue.length) {
    const [start, dur] = queue.shift();
    currentTime = Math.max(currentTime + dur, start + dur);
    totalResponseTime += currentTime - start;

    while (tasks.length && tasks[0][0] <= currentTime) {
      queue.push(tasks.shift());
      queue.sort((a, b) => a[1] - b[1]);
    }

    if (tasks.length && !queue.length) {
      queue.push(tasks.shift());
      queue.sort((a, b) => a[1] - b[1]);
    }
  }

  return parseInt(totalResponseTime / jobs.length);
}

console.log(
  solution([
    [1, 9],
    [0, 3],
    [2, 6],
  ]),
  9
);
