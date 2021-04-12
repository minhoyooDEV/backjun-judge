function func(A) {
  const map = new Map();

  for (let num of A) {
    let n = num;
    let sum = 0;

    while (n > 0) {
      sum += n % 10;
      n = parseInt(n / 10);
    }

    const list = map.get(sum);
    if (list) {
      list.push(num);
    } else {
      map.set(sum, [num]);
    }
  }

  let max = -1;

  map.forEach((values, key) => {
    if (values.length >= 2) {
      values.sort((a, b) => b - a);
      max = Math.max(values[0] + values[1], max);
    }
  });

  console.log(max);
  return max;
}

func([51, 71, 17, 42]);
func([42, 33, 60]);
func([51, 32, 43]);
