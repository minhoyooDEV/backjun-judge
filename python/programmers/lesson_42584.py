def solution(prices):
    answer = []

    for i in range(0, len(prices) - 1):
        count = 0
        exp_price = prices[i]
        for j in range(i + 1, len(prices)):
            cmp_price = prices[j]

            # print(exp_price, cmp_price, count)
            if exp_price <= cmp_price:
                count += 1
            else:
                count += 1
                break

        answer.append(count)
    answer.append(0)

    return answer


print(solution([1, 2, 3, 2, 3]))
