async function runsequentially(functions) {
  try {
    return await functions.reduce(async (acc, f) => {

      const result = await f()
      return acc.then(ac => Promise.resolve([...ac, result]))

    }, Promise.resolve([]))
  } catch (error) {
      throw error
  }
}

let counter =1;
let hasFaild = false;
function incrementCounterAsync() {
  return new Promise((resolve, reject) => {
    counter +=1;
    // if (counter === ) {
    //   reject('error')
    // }
    resolve(counter)
  })
}

let promise = runsequentially([incrementCounterAsync, incrementCounterAsync, incrementCounterAsync])
if (promise) {
  promise.then(result => console.log(result))
  .catch(error => console.log("Error: " + error))
}