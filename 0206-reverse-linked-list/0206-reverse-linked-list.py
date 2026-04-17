# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr = None, head
        while curr:
            next = curr.next ## need to store next before reversing current next
            curr.next = prev
            prev = curr
            curr = next
        return prev

        