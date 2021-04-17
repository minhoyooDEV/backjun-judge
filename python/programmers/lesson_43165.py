def solution(numbers, target):
    answer = 0

    def dfs(idx: int, result: int):
        if idx == (len(numbers)):
            if result == target:
                return 1
            return 0
        else:
            value = numbers[idx]
            return dfs(idx + 1,  result + value) + dfs(idx + 1,  result - value)

    answer = dfs(0,  0)

    print(answer)
    return answer


solution([1, 1, 1, 1, 1]	, 3)
