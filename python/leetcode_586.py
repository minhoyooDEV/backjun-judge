# 다풀어놓고 문제해석을 잘못해서 마무리를 못했다.

class Solution:

    def kWeakestRows(mat, k):
        # 군인수와 오리지널 로우를 저장
        original_soliders = []
        for i in range(len(mat)):
            original_soliders.append((i, sum(mat[i])))

        modified_info = sorted(original_soliders, key=lambda x: x[1])
        # result = []
        # for info in modified_info:
        #   if (info[0] <= original_soliders[k][0]) and (info[1] <= original_soliders[k][1]):
        #         result.append(info[0])

        # return result
        answer = [idx[0] for idx in modified_info[:k]]
        return answer





print(Solution.kWeakestRows([[1, 1, 0, 0, 0],
                             [1, 1, 1, 1, 0],
                             [1, 0, 0, 0, 0],
                             [1, 1, 0, 0, 0],
                             [1, 1, 1, 1, 1]], 3))

print(Solution.kWeakestRows([[1, 0, 0, 0],
                             [1, 1, 1, 1],
                             [1, 0, 0, 0],
                             [1, 0, 0, 0]], 2))






print(Solution.kWeakestRows([[1, 1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1, 1]], 1))

# 최적화코드
# class Solution:
#     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#         d = {}

#         for i in range(len(mat)):
#             d[i] = sum(mat[i])

#         return sorted(d, key=d.get)[:k]