var fs = require('fs');
console.log('123123')
var input = fs.readFileSync('/dev/stdin').toString().split('\n');
var count = parseInt(input[0]);
console.log(count)

var list = [];
for (var i = 0; i < count; i++) {
    list.push(input[i + 1])
}
list.sort()
list.foreach(v => console.log(v))
