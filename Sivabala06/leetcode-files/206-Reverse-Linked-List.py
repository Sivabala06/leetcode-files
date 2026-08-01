# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, pointer=None):
#         self.val = val
#         self.next = 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_node=head
        prev=None
        while cur_node is not None:
            next_node=cur_node.next
            cur_node.next=prev
            prev=cur_node
            cur_node=next_node
        return prev
                
        