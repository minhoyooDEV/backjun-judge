// const fs = require('fs');
// const s = fs.readFileSync('/dev/stdin').toString()
const s = 'backjun'
const a = 'a'.charCodeAt(0), b = 'z'.charCodeAt(0);
const result = []
for (let i = a; i <= b; ++i) {
    result.push(0);
}
console.log(a)
for (const c of s) {
    console.log(c, c.charCodeAt(0))
    console.log(c.charCodeAt(0) - a)
    result[c.charCodeAt(0) - a] += 1
}

console.log(result.join(' '))