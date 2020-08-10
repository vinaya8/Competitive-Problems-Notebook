#Remove nth node from last from linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n==1 and head.next==None:
            return None
        
        curr=ListNode()
        curr=head
        for i in range(n-1):
            curr=curr.next
        
        remove=head
        prev=ListNode()
        
        while curr.next!=None:
            curr=curr.next
            prev=remove
            remove=remove.next
        
        if remove==head:
            head=head.next
            return head
        
        prev.next=remove.next
        
        return head