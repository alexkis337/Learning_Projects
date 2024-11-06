# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(head):
        if str(head) == str(head)[::-1]:
            return True
        else:
            return False

print(Solution.isPalindrome(133451))