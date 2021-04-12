function func(A = [], X, Y, Z) {
  let maxX = (maxY = maxZ = time = 0);

  const maxD = Math.max(X, Y, Z);

  const map = new Map();

  while (true) {
    for (let i = 0; i < A.length; i++) {
      const car = A[i];
      if (car != 0 && car <= X && time >= maxX) {
        X -= car;
        map.set(i, time);
        maxX += car;
        A[i] = 0;
        break;
      }
    }
    for (let i = 0; i < A.length; i++) {
      const car = A[i];
      if (car != 0 && car <= Y && time >= maxY) {
        Y -= car;
        map.set(i, time);
        maxY += car;
        A[i] = 0;
        break;
      }
    }
    for (let i = 0; i < A.length; i++) {
      const car = A[i];
      if (car != 0 && car <= Z && time >= maxZ) {
        Z -= car;
        map.set(i, time);
        maxZ += car;
        A[i] = 0;
        break;
      }
    }

    time += 1;

    if (time > maxD) break;
  }
  const result = map.size != A.length ? -1 : map.get(A.length - 1);
  return result;
}

func([2, 8, 4, 3, 2], 7, 11, 3);
