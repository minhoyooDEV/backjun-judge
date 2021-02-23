// 처음에는 s를 기준으로 d를 판단하려 했으나 더 복잡해진다는 판단에 d를 순회하기로 결정
// 데이터의 양이 많지않으므로 O(n2)으로 풀어도 된다고 생각했다.
// 모범답안 1, 2, 3(특히) 은 참고하면 좋을 것 같다

function findLongestWord(s: string, d: string[]): string {
    if (!d.length) {
        return ''
    }
    const orderedD = d.sort();
    
    let targetIndex = 0;
    let maxLength = 0;
    
    orderedD.forEach((str, odIndex) => {
        let start = 0
        s.split('').forEach((ch, i) => {
            if ( ch === str.split('')[start]) {
                start += 1
            }
            if (str.length === start && str.length > maxLength) {
                maxLength = str.length;
                targetIndex = odIndex;
            }
        })
    })
    
    if (maxLength) {
        return orderedD[targetIndex]   
    } else {
        return ''
    }
};



// function findLongestWord(s: string, d: string[]): string {

//     /*d.sort((a, b) => {
        
//         if(a.length != b.length) return (b.length - a.length)
//         return a < b ? -1 : 0
//     })*/
    
    
//     // Sorted as per length and lexico
//     let result = ""
//      1. 제시 답보다 긴 경우는 배제시킴
//     for (const dw of d) {
//         if (dw.length > s.length) {
//             continue
//         }
//         let i = 0
//         let j = 0
//         while (j < s.length && i < dw.length) {
//              
//             if(s[j] === dw[i]){
//                 i++
//             }
//             j++
//         }
//         if (i === dw.length && dw.length >= result.length) {
//             if (dw.length > result.length) {
//                  2. 길이를 판단하는기준
//                 result = dw
//             } else if (dw < result) {
//                 3. 알파벳 순서를 판단 하는 기준
//                 result = dw // lexico
//             }
//         }        
//     }
        
//     return result
    
// };