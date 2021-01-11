case_count = int(input())

for _ in range(case_count):
    stack = []
    data = list(input())
    if (len(data) % 2) == 1:
        print('NO')
        continue

    isBreaked = False
    for i in range(len(data)):
        if data[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(data[i])
        else:
            stack.append(data[i])

        if stack:
            print('NO')
        else:
            print('YES')
