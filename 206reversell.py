# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        temp = head
        while temp.next:
            n = temp.next
            temp.next = n.next
            n.next = head
            head = n

        return head
        


        