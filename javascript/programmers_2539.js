// 단순구현으로 차근차근 풀다보니 해결함

function solution(priorities, location) {
    var answer = 0;
    let queue = [];
    
    const pairs = priorities.map((p, i) => [p, i]) //save initial info
    
    let i = 0;
    let printIndex = 0
    for (let p = 9; p > 0; p--){
        i = printIndex;
        for (let c = pairs.length; c > 0; c--) {
            if (pairs[i][0] === p) {
                queue.push(pairs[i])
                printIndex = i
            }    
            i++
            if (i === pairs.length) {
                i = 0
            }
        }
    }
    for (let i = 0; i < queue.length; i++) {
        if (queue[i][1] === location) {
            return i + 1
        }
    }
    return answer;
}