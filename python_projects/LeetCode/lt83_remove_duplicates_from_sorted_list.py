class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head=ListNode()):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

x = Solution()
print(x.deleteDuplicates([1,1,2]))

# elem = 0
# while elem < len(head):
#     if head[elem] == head[elem - 1]:
#         print(elem)
#         head = head.pop(elem - 1)
#         elem -= 1
# return head