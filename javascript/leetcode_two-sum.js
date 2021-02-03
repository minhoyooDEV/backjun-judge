/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    if (nums.length == 2) {
        return [0, 1]
    }
    let result = [];
    for (aIndex in nums){
        console.log({aIndex})
        const a = nums[aIndex];
        for (bIndex in nums){
            const b = nums[bIndex];
            if ((a + b) === target) {
                result.push(aIndex);
                result.push(bIndex);
                break
            }
        }
        
        if (result.length) {
            break
        }
    }
    return result;
};

console.log(twoSum([2,7,4,3,1], 9))

