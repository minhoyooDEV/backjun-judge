// You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

// You are given an integer array nums representing the data status of this set after the error.

// Find the number that occurs twice and the number that is missing and return them in the form of an array.

// 체크를 할 수 있는 영역을 만든뒤 비교를 해서 없애나가며 해결했다
// 제출답안중 더하기로 푸는 방법이 있었는데 참고해봐도 좋을것 같다.

function findErrorNums(nums: number[]): number[] {
    const dupNums = Array(nums.length + 1).fill(true)
    
    let repetition = 0
    let loss = 0
    for (const num of nums) {
        if (dupNums[num]) {
            dupNums[num] = false
        } else {
            repetition = num
        }
    }

    for (let i = 1; i < dupNums.length; i++){
        if (dupNums[i]) {
            loss = i
            break
        }
    }
    return [repetition, loss]
    
};


// function findErrorNums(nums: number[]): number[] {
//     let set = new Set<number>();
//     let sum = 0;
//     let dup = 0;

// //  중복을 체크하는건 같다
//     for (let num of nums) {
//         if (set.has(num)) dup = num;
//         set.add(num);
//         sum += num;
//     }
// // 1부터 n까지 정상적으로 다 더한값
//     let sum2 = (1 + nums.length) * nums.length / 2;
//     return [dup, sum2 - sum + dup];
// };