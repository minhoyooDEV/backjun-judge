function solution(operations) {
  const queue = [];

  for (const op of operations) {
    let [cmd, number] = op.split(" ");
    number = +number;
    console.log({ cmd, number });
    if (cmd === "I") {
      queue.push(number);
    } else if (cmd === "D") {
      if (number > 0) {
        if (queue.length) queue.sort((a, b) => b - a);
      } else {
        if (queue.length) queue.sort((a, b) => a - b);
      }
      queue.shift();
    }
  }
  if (queue.length) {
    queue.sort((a, b) => a - b);
    return [queue[queue.length - 1], queue[0]];
  }
  return [0, 0];
}
console.log(solution(["I 16", "D 1"]));
console.log(solution(["I 7", "I 5", "I -5", "D -1"]));
