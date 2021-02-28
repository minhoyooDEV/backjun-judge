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


def search_target(ary, target):
    print(ary)
    if len(ary) == 1 and target == ary[0]:
        return True
    if len(ary) == 1 and target != ary[0]:
        return False
    if len(ary) == 0:
        return False
    
    mid = len(ary) //2
    if target == ary[mid]:
        return True
    else:
        if target > ary[mid]:
            return search_target(ary[mid:], target)
        else:
            return search_target(ary[:mid], target)
