// 
// function searchMatrix(matrix: number[][], target: number): boolean {
//     // const checkedMatrix = Array(matrix.length).fill(Array(matrix[0].length).fill(false))
//     // console.log(checkedMatrix)
//     for (const ary of matrix) {
//         for (const n of ary) {
//             if (n === target) {
//                 return true;
//             }
//         }
//     }
//     return false
    
// };

function searchMatrix(matrix: number[][], target: number): boolean {
    // x의 초기값은 가장 작은범위
    // y의 초기값은 가장 큰 범위에 셋팅한다
    let x, y;
    x = 0;
    y = matrix[0].length - 1;
    
    while (x < matrix.length && y >= 0) {
        // 해당값을 찾으면 true리턴
        if (matrix[x][y] === target) {
            return true;
        } else if (matrix[x][y] < target) {
            // 해당값보다 작다면 오른쪽으로 한칸이동
            x++;
        } else {
            // 해당값보다 크다면 위로ㅋ으로 한칸이동
            y--;
        }
    }
    
    return false;
};