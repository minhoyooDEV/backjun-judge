s = list(input())
text = input()

stack = []

# ['m', 'i', 'r', 'k', 'o', 'v', 'C', '4', 'n', 'i', 'z', 'C', 'C', '4', '4']
# print(s)
# ['m']
# print(s[:1])
# ['i', 'r', 'k', 'o', 'v', 'C', '4', 'n', 'i', 'z', 'C', 'C', '4', '4']
# print(s[1:])
# ['m', 'i', 'r', 'k', 'o', 'v', 'C', '4', 'n', 'i', 'z', 'C', 'C', '4', '4']
# print(s[:])
# ['4']
# print(s[-1:])
# ['m', 'i', 'r', 'k', 'o', 'v', 'C', '4', 'n', 'i', 'z', 'C', 'C', '4']
# print(s[:-1])

for i in range(len(s)):
    ch = s[i]
    stack.append(ch)

    if len(stack) >= len(text_l):
        if ch == text_l[-1]:
          target = stack[-len(text_l):]
          if ''.join(target) == text:
            # stack = stack[:-len(text_l)] 이 부분에서 시간복잡도 증가
            del stack[-len(text_l):] #끝에서 해당부분을 삭제한다

if stack:
  print(''.join(stack))
else:
  print("FRULA")