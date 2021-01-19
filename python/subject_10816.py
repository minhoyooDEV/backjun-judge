n = int(input())
n_nums = list(map(int, input().split(' ')))
m = int(input())
m_nums = list(map(int, input().split(' ')))

d = {}
for n_num in n_nums:
    if n_num in d:
        d[n_num] += 1
    else:
        d[n_num] = 1

result = ''
for m_num in m_nums:
    s = ' '
    if m_num in d:
        s += str(d[m_num])
    else:
        s += str(0)

    result += s


print(result.strip())
