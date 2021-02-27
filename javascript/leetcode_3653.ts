
// Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.
// Example 1:

// Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
// Output: true
// Explanation: We might do the following sequence:
// push(1), push(2), push(3), push(4), pop() -> 4,
// push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
// 
// 스택의 구조를 알면 어렵지않게 풀수 있었던것 같다. 당황하지 않고 차근차근 풀어보자



function validateStackSequences(pushed: number[], popped: number[]): boolean {
    const stack = [];
    
    let i = 0
    for (const num of pushed) {
        
        stack.push(num)
        
        while(stack.length &&stack[stack.length-1] === popped[i] ){
            stack.pop()
            i++
        }
    }
    return stack.length ? false : true;
};