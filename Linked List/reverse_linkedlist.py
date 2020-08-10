#Reverse a Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev=ListNode()
        curr=ListNode()
        prev=None
        curr=head
        temp=ListNode()
        while curr!=None:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        return prev