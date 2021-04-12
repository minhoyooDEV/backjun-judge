# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l = [head]
        while head.next:
            l.append(head.next)
            head = head.next

        for i in range(len(l)//2):
            if l[i].val != l[-(i + 1)].val:
                return False

        return True

# class Solution2:
#     def isPalindrome(self, head: ListNode) -> bool:
#         vals = []
#         while head != None:
#             vals.append(head.val)
#             head = head.next
#         return vals == vals[::-1] # 역순으로