// 완주하지 못한자

// 다른 풀이에 정렬로 해법이 있었지만, sort에서 O(logN) 성능저하가 일어나서 O(n) 보다는 느렸다.


function solution(participant, completion) {
    const map = new Map();
    participant.forEach(person => {
        map.set(person, (map.get(person) || 0) + 1)
    })
    completion.forEach(person => {
        map.set(person, map.get(person) - 1)
    })
    let answer = '';

    for (const [k, v] of map){
        if (v !== 0 ) {
            answer = k;
        }
    }
    return answer;
}