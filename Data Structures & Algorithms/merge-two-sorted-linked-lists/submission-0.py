# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode()
        curr1 = list1
        curr2 = list2
        head = out

        while curr1 and curr2:
            if curr1.val<=curr2.val:
                out.next = ListNode(curr1.val)
                out = out.next
                curr1 = curr1.next
            elif curr1.val>curr2.val:
                out.next = ListNode(curr2.val)
                out = out.next
                curr2 = curr2.next
        
        while curr1:
            out.next = ListNode(curr1.val)
            out = out.next
            curr1 = curr1.next

        while curr2:
            out.next = ListNode(curr2.val)
            out = out.next
            curr2 = curr2.next
        
        return head.next