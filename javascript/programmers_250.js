// 스택으로 쉽게 풀수있었다.
function solution(s)
{
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    if (s.length === 0 || s.length % 2 === 1) {
        return 0;
    }
    const stack = [];

    for (const ch of s){
        if (stack.length && stack[stack.length -1] === ch) {
            stack.pop()
        } else {
            stack.push(ch)
        }
    }

    return stack.length ? 0 : 1;
}