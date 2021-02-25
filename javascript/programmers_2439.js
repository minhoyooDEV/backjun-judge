function solution(msg) {
    var answer = [];
    let data = new Map();
    let index = 1
    for (let codeNum = "A".charCodeAt(); codeNum <= "Z".charCodeAt(); codeNum++) {
        data.set(String.fromCharCode(codeNum), index)
        index++
    }
    let w = msg[0]
    for (let i = 1 ; i < msg.length; i++) {
        let c = msg[i];
        let wc = ''
        if (data.get(w)) {
            answer.push(data.get(w)) // 출력
            wc = w+c;
            if (data.get(wc)){
                
            } else {
                data.set(wc,index);
                index++;    
            }
            
            w = c;
        }
    }
    
    return answer;
}