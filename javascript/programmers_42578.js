//  위장

// 데이터를 우선 기록한다음에 

// 발생할 수 있는 경우의 수를 찾는다.
// 발생할 수 있는 경우의 수를 찾는 공식이 핵심인 것 같다.


function solution(clothes) {
    const map = new Map();
    
    for (const data of clothes) {
        const [name, category] = data;
        if (map.has(category)){
            map.get(category).push(name);
        } else {
            map.set(category, [name]);
        }
    }
    var answer = 1;
    map.forEach((ary) => {
        answer = answer * (ary.length + 1);
    })
    
    return answer - 1;
}