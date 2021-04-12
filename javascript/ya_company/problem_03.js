function func(A = []) {
  const chekced = Array(A.length + 1).fill(false);
  chekced[0] = true;

  let count = 0;

  for (const a of A) {
    chekced[a] = true;

    let result = true;
    for (let i = 1; i <= a; i++) {
      result = result && chekced[i];
    }
    if (result) count++;
  }

  console.log(count);
  return count;
}

func([2, 1, 3, 5, 4]); // 3
func([2, 3, 4, 1, 5]); // 2
func([1, 3, 4, 2, 5]); // 3
