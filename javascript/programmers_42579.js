// 베스트앨범

// 문제를 잘못이해해서 시간을 많이 끌었다.
// 장르마다 1개 또는 2개씩 넣는것이었다.

function solution(genres, plays) {
    var answer = [];
    
    const o = {}
    for (let i = 0; i < genres.length; i++) {
        const genre = genres[i];
        const play = plays[i];
        const tuple = [play, i]
        if (o[genre]) {
            o[genre].data.push(tuple);
            o[genre].count += play;
        } else {
            o[genre] = {
                key: genre,
                count: play,
                data:[tuple]
            }
        }       
    }
    const ranks = Object.values(o).sort((a, b) => (b.count - a.count));
    
    for (let i = 0; i < (ranks.length > 1 ? ranks.length : 1); i++) {
        const data1 = ranks[i].data;
        if (data1.length > 1) {
            
            data1.sort((a, b) => a[1] - b[1]).sort((a, b) => b[0] - a[0])

            answer.push(data1[0][1])
            answer.push(data1[1][1])
        } else {
            answer.push(data1[0][1]);
        }
    }    
    
    return answer;
}