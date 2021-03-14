# 프로그래머스 - 가장 큰 수 

from typing import Literal


def solution1(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))

print(solution1([6,10,2]))
print(solution1([92,91,9]))
print(solution1([0,0]))

def solution2(intervals):
    intervals.sort()

    result = []
    for interval in intervals:
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    
    return result





print(solution2([[1,3],[2,6],[8,10],[15,18]]))
print(solution2([[1,3],[2,6],[8,10],[15,18],[19,19]]))
print(solution2([[1,3],[2,6],[8,10],[15,18],[20,20]]))
print(solution2([[1,3],[2,6],[8,10],[15,18],[20,20]]))
print(solution2([[1,4],[4,5]]))
print(solution2([[1,4],[5,6]]))



def solution4(beginWord, endWord, wordList):
    if not endWord in wordList:
        return 0
    g = {}
    for word in wordList:
        for i in range(len(word)):
            key = word[:i] + '_' + word[i+1:]
            if not g.get(key):
                g[key] = []
            g[key].append(word)

    q = [(beginWord, 1)]
    visited = []
    
    print(g)
    while q:
        word, depth = q.pop(0)

        if word == endWord:
            return depth
        
        if word in visited:
            continue

        visited.append(word)

        for i in range(len(word)):
            key = word[:i] + '_' + word[i+1:]
            if g.get(key):
                for word2 in g[key]:
                    q.append((word2, depth + 1))
        
    return 0

    # while q
# print(solution("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
# print(solution("hot","dog",["hot","dog"]))
# print(solution("hit","cog",["hot","dot","dog","lot","log","cog"]))
