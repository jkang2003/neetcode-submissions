# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        curr = head

        while(curr):
            nums.append(curr.val)
            curr = curr.next
        
        if not nums:
            return curr

        rhead = ListNode(nums[-1])
        rcurr = rhead
        for i in range(len(nums) - 2, -1, -1):
            rcurr.next = ListNode(nums[i])
            rcurr = rcurr.next
        
        return rhead