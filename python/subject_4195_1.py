# 시간초과

case = int(input())


for _ in range(case):
    f = int(input())

    l = []
    for i in range(f):
        a, b = input().split(' ')

        set = {}
        info_a, info_b = None, None
        for i in range(len(l)):
            g=l[i]
            if a in g:
                info_a=i
            if b in g:
                info_b=i

        if info_a != None and info_b != None:
            g_a=l[info_a]
            g_b=l[info_b]
            g_a |= g_b
            l[info_a]=g_a
            print(len(l[info_a]))
            del l[info_b]
        elif info_a != None:
            l[info_a].add(b)
            print(len(l[info_a]))
        elif info_b != None:
            l[info_b].add(a)
            print(len(l[info_b]))
        else:
            l.append({a, b})
            print(2)
