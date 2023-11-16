# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        return (sorted(list1+list2))


x = Solution()
print(x.mergeTwoLists([1,2,4],[1,3,4]))
