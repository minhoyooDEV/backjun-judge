case = int(input())

l = [0]*(case)

l_height, l_count = 0, 0
r_height, r_count = 0, 0

for i in range(len(l)):
    l[i] = int(input())

    if l_height < l[i]:
        l_height = l[i]
        l_count += 1
r_l = list(reversed(l))
for i in range(len(r_l)):
    if r_height < r_l[i]:
        r_height = r_l[i]
        r_count += 1

print(l_count)
print(r_count)
