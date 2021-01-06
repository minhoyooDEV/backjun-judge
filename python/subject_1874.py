n = int(input())

qList = []
for _ in range(n):
  qList.append(int(input()))

pointer = 0
result = []
stack = []
count = 1
for n in range(1, n + 1):
  targetNum = qList[n]

  while count <= targetNum:
    if len(stack) == 0:
      stack.append(targetNum)
      count+=1
      result.append('+')

  if targetNum > stack[-1]:
    stack.append(n)
    n+=1
    result.append('+')

  if pointer >= n:
    break

print(result)
print('NO')
