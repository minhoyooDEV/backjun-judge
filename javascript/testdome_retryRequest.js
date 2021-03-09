async function retryRequest(promiseFunc, nrOfRetries) {
  if (nrOfRetries === 0) {
    return Promise.reject(0)
  }
  nrOfRetries--;
  try {
    const res = await promiseFunc();
    return res;
  } catch {
    return retryRequest(promiseFunc, nrOfRetries)
  }

}

let hasFaild = false;
function getUserInfo() {
  return new Promise((resolve, reject) => {
    if (!hasFaild) {
      hasFaild = true;
      reject("Exception!");
    } else {
      resolve("Fetched user");
    }
  })
}

let promise = retryRequest(getUserInfo, 3);
if (promise) {
  promise.then(result => console.log(result))
  .catch(error => console.log('Error'));
}