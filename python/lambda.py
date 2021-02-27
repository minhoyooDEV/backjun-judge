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

sss = 'FastCampus'
res = sss[3:]
print(res)
aryt = [1,2,3,4,5,6,7,8,9]
print(aryt[0], aryt[-1])
print(aryt[1:])

