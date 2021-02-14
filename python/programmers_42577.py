# 단순 반복외에는 방법이 없을 것 같았는데
# 한번 정렬을 한 후에 처리를 하면 복잡도를 낮출 수 있는 것 같다.


# def solution(phone_book):

#     answer = True

#     for p_i in range(len(phone_book)):
#         if not answer:
#             break
#         for p_j in range(len(phone_book)):
#             i = phone_book[p_i]
#             j = phone_book[p_j]
#             if p_i == p_j:
#                 continue
#             elif len(i) > len(j):
#                 continue
#             else:
#                 if i == j[:len(i)]:
#                     answer = False
#                     break

#     return answer


# def solution(phone_book):
#     for i in range(len(phone_book)):
#         pivot = phone_book[i]
#         for j in range(i+1, len(phone_book)):
#               strlen = min(len(pivot), len(phone_book[j]))
#               if pivot[:strlen] == phone_book[j][:strlen]:
#                   return False
#         return True
