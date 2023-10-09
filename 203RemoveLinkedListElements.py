# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next =head)
        temp = head
        prev = dummy
        while temp:
            nxt = temp.next
            if temp.val == val:
                prev.next = nxt
            else:
                prev = temp
            temp = nxt

        return dummy.next

        
