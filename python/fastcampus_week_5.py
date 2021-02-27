# 1. 이진 탐색법은 정렬된 자료를 탐색하는 데에 사용할 수 있다. 인덱스가 낮을 수록 더 작은 값으로 정렬된 2차원 리스트에서 target을 찾으면 True를 반환하고, target을 찾을 수 없으면 False를 반환하는 프로그램을 작성하시오.


def searchMatrix(matrix, target):
    length = len(matrix)
    mid = length // 2
    ary = matrix[mid]

    if mid == 0:
        return search_target(ary, target)

    min, max = ary[0], ary[-1]
    
    if target < min:
        return searchMatrix(matrix[:mid], target)
    elif target > max:
        return searchMatrix(matrix[mid:], target)
    else:
        return search_target(ary, target)

def search_target(ary, target):
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
        if target < ary[mid]:
            return search_target(ary[:mid], target)
        else:
            return search_target(ary[mid:], target)



print(searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 3))
print(searchMatrix([[0]], 0))
print(searchMatrix([[0], [1], [2]], 1))
print(searchMatrix([[0], [2]], 1))
print(searchMatrix([[0], [2], [3], [5]], 4))


# 2. 두 문자열 A와 B가 있을 때, 두 문자열의 '최대공약문자열' C를 아래와 같이 정의하자.

# 문자열 C를 반복하여 문자열 A와 B를 생성할 수 있다.
# 가능한 C 중에 가장 긴 문자열을 C로 한다.
# 위 조건을 만족하는 C가 없으면 빈 문자열을 C로 한다.
# 이 때, 문자열 A와 B를 입력받아 C를 출력하는 프로그램을 작성하시오.
def gcdString(A, B):
    if len(A) < len(B):
        return gcdString(B, A)
    elif not A.startswith(B):
        return ''
    elif len(B) == 0:
        return A
    else:
        return gcdString(A[len(B):], B)


print(gcdString('aaaa', 'b'))
print(gcdString('ababab', 'abab'))
print(gcdString('abababab', 'abab'))
# print(gcdString('b', 'aaaa'))


# 3. n개의 노드가 있는 그래프가 있다. 각 노드는 1부터 n까지 번호가 적혀있다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 한다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미한다.

# 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성하라.

# 제한사항

# 노드의 개수 n은 2 이상 20,000 이하입니다.
# 간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
# vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.

import heapq
# 과제 3번 코드란
def solution3(n, vertex):
    g = {}

    for data in vertex:
        a, b = data
        if not g.get(a):
            g[a] = [b]
        else:
            g[a].append(b)

        if not g.get(b):
            g[b] = [a]
        else:
            g[b].append(a)

    distances = {node: float('inf') for node in g}
    distances[1] = 0
    q = []
    heapq.heappush(q, [distances[1], 1])


    while q:
        current_distance, current_node = heapq.heappop(q)
        if distances[current_node] < current_distance:
            continue

        for adjacent in g[current_node]:
            distance = current_distance + 1
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(q, [distance, adjacent])
    par_max = max(distances.values())
    result = 0
    for v in distances.values():
        if v == par_max:
            result += 1

    return result

print(solution3(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	) )
print(solution3(7, [[7, 6], [3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
print(solution3(7, [[7, 1], [3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
print(solution3(7, [[1, 7], [3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
print(solution3(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]) )
print(solution3(2, [[1,2], [1,3] ]) )
print(solution3(2, [[1,2], [2,3] ]) )


# 4. 마을에 1부터 N의 고유 번호를 가진 사람들이 있다. 소문으로는 마을 사람 중에 마을 판사가 있다고 한다. 마을 판사가 실제로 존재한다면,

# 마을 판사는 아무도 믿지 않는다.
# 다른 모든 사람들은 마을 판사를 믿는다.
# 마을 판사가 있다면 오직 한명 뿐이다.
# 리스트 trust가 주어졌을 때, trust[i] = [a, b]는 고유 번호가 a인 사람이 고유 번호가 b인 사람을 믿는다는 것을 의미한다고 한다.

# 마을 판사가 존재한다면 마을 판사의 고유 번호를, 존재하지 않는다면 -1을 출력하는 프로그램을 작성하시오.

# (단, a가 b를 믿고 b가 c를 믿는다고 할 때, a가 c를 믿는다는 의미는 아니다.)


def solution4(N, trust):
    trust_g = {}
    trusted_g = {}
    for ary in trust:
        a, b = ary

        if trust_g.get(a):
            trust_g[a].append(b)
        else:
            trust_g[a] = [b]

        if trusted_g.get(b):
            trusted_g[b].append(a)
        else:
            trusted_g[b] = [a]
    
    candidates = [a for a in trusted_g if len(trusted_g[a]) == (N-1) ]
    
    # print('candidates', candidates)
    # print('trust_g', trust_g)
    # print('trusted_g', trusted_g)
    
    result = -1
    if candidates:
        for candidate in candidates:
            if not trust_g.get(candidate):
                result = candidate
                break
    # print('result', result)
    return result

solution4(2, [[1,2]])
solution4(3, [[1,3],[2,3]])
solution4(3, [[1,3],[2,3], [3,2], [1,2]])
solution4(3, [[1,3],[2,3],[3,1]])
solution4(3, [[1,2],[2,3]])
solution4(4, [[1,3],[1,4],[2,3],[2,4],[4,3]])
solution4(4, [[1,3],[1,4],[2,3],[2,4],[4,3], [3,1]])



