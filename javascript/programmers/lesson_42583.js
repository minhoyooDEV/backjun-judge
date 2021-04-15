function solution(bridge_length, weight, truck_weights) {
  const queue = Array(bridge_length).fill(0);

  let time = 0;
  const totalTruncks = truck_weights.length;
  const outtedTrucks = [];
  while (outtedTrucks.length < totalTruncks) {
    const truck = truck_weights[0];

    const outtedTruck = queue.shift();

    if (queue.reduce((prev, v) => prev + v, 0) + truck <= weight) {
      queue.push(truck_weights.shift());
    } else {
      queue.push(0);
    }

    time += 1;

    if (outtedTruck) {
      outtedTrucks.push(outtedTruck);
    }
  }

  return time;
}
console.log(solution(2, 10, [7, 4, 5, 6]), 8);
