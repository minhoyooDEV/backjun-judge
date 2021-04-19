// stack

/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var removeDuplicates = function (s, k) {
  const stack = [];

  for (let i = 0; i < s.length; i++) {
    const ch = s[i];

    if (stack.length) {
      const head = stack[stack.length - 1]
      const headCh = stack[stack.length - 1][0]
      let headCount = stack[stack.length - 1][1]

      if (headCh === ch) {
        if ((headCount + 1) === k) {
            while(headCount) {
              headCount--
              stack.pop()
            }
        } else {
          stack.push([ch, headCount + 1])
        }
      } else {
        stack.push([ch, 1])
      }
    } else {
      stack.push([ch, 1]);
    }

    console.log(stack)
  }
  return stack.map(d => d[0]).join('');
};

// console.log(removeDuplicates('deeedbbcccbdaa', 3));
// console.log(removeDuplicates('pbbcggttciiippooaais', 2));

var removeDuplicates2 = function (s, k) {
  let stack = [];
  s = s.split('');
  for (let i = 0; i < s.length; ++i) {
    if (i == 0 || s[i] !== s[i - 1]) {
      stack.push(1);
    } else {
      stack[stack.length - 1]++;

      if (stack[stack.length - 1] === k) {
        stack.pop();
        s.splice(i - k + 1, k);

        console.log({i, k, ik: i-k, ik2: i-k + 1})
        i = i - k;
      }
    }
    console.log(stack, s.join(''))
  }
  return s.join('');
};
console.log(removeDuplicates2('deeedbbcccbdaa', 3));