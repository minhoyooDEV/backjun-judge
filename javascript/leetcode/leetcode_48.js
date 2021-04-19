/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
 var rotate = function(matrix) {
  const length = matrix.length
  if (length === 1) {
      return matrix
  }

  const half = parseInt(length / 2)
  const output = Array(length).fill(Array(length).fill(0))

  for (const row in matrix) {
      // const halfRow = parseInt(row / 2)

      for (const col in matrix[row]) {
          // let newRow =
          // let newCol =
          const val = matrix[row][col];
          let pos = 1
          if (  row <half) {
              // if (col < half) {
                pos = 1
              // } else {
              //   pos = 2
              // }
          }else {
              // if (col < half) {
                pos = 3
              // } else {
              //   pos = 4
              // }

          }
          console.log(pos, val)

          // output[][]= matrix[row][col]
      }
  }
};

// console.log(solution([[1,2],[3,4]]))
console.log(rotate([[1,2,3],[4,5,6],[7,8,9]]))
// console.log(solution([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))