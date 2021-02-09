def lambdaA(a, b):
    return a**2 * b


print(lambdaA(2, 3))

l = []
if l:
    print(l)
else:
    print('Nah.')

l.append('1')

if l:
    print(l)
else:
    print('Nah.')

print('================')
ss1 = str(-123)
print(ss1)
print(ss1[0], ss1[:1], ss1[-1])
for i in range(int(len(ss1) / 2)):
    print(ss1[i], ss1[-(i+1)])
    # if ss1[i] != ss1[-(i+1)]:
    #     print
