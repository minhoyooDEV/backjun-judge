import sys
count = int(input())

stack = []
for i in range(count):
  data = list(sys.stdin.readline().rstrip().split(' '))
  cmd = data[0]

  if cmd == 'push':
    stack.append(data[1])
  elif cmd == 'pop':
    if len(stack):
      print(stack.pop())
    else:
      print(-1)
  elif cmd == 'size':
    print(len(stack))
  elif cmd == 'empty':
    if len(stack):
      print(0)
    else:
      print(1)
  elif cmd == 'top':
    if len(stack):
      print(stack[-1])
    else:
      print(-1)