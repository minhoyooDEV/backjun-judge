function startTimer(callback, interval) {
  // Write the code that goes here
  console.log('run!!')
  let value = 0

  const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        const res = callback(value)
        if (res) {
          resolve(res)
        }
      resolve()
    }, interval)
  })
  promise.then(0)
}

function callback(counter) {
  console.log(counter);

  return counter < 5;
}

// Expected: 1, 2, 3, 4, 5 with 50ms interval.
startTimer(callback, 1000);