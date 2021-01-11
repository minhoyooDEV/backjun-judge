case_count = int(input())

for _ in range(case_count):
  stack = []
  data = list(input())
  if (len(data) % 2) == 1:
    print('NO')
    continue

  isBreaked = False
  for i in range(len(data)):
    if data[i] == '(':
      stack.append(data[i])
    elif data[i] == ')':
      if len(stack):
        if stack[-1] == '(':
          stack.pop()

      else:
        print('NO')
        isBreaked = True
        break

  if not (isBreaked) :
    if len(stack):
      print('NO')
    else:
      print('YES')
