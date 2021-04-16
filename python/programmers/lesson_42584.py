def solution(prices):
    answer = [0] *  len(prices)

    stack = []

    for i, price in enumerate(prices):
      if len(stack) == 0 :
        stack.append((price, i))
      elif stack[-1][0] <= price:
        stack.append((price, i))
      else:
        for j in range(i, -1, -1):
          if stack[j -1][0] > price:
              stack.pop()
          else:
            stack.append(price, i)
            break

      print(stack)
      # for d in stack:
      #   price, inx = d
      #   answer[inx] += 1

    return answer


print(solution([1, 2, 3, 2, 3]))