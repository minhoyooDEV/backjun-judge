const fs = require('fs');
const s = fs.readFileSync('/dev/stdin').toString()
const a = 'a'.charCodeAt(0), b = 'z'.charCodeAt(0);
const result = []
for (let i = a; i <= b; ++i) {
    result.push(0);
}
for (const c of s) {
    result[c.charCodeAt(0) - a] += 1
}

console.log(result.join(' '))