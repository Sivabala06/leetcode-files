# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        cur1=l1
        sum1=sum2=0
        place1=place2=1
        
        while (cur1 is not None ):
            sum1+=(place1*cur1.val)
            place1*=10
            cur1=cur1.next

        cur2=l2
       
        while (cur2 is not None ):
            sum2+=(place2*cur2.val)
            place2*=10
            cur2=cur2.next
        
        tot=sum2+sum1
        print(tot)
        if tot ==0:
            return ListNode(0)
        dig=tot%10
        tot=tot//10  
        ans=ListNode(dig)
        cur=ans
        while tot!=0:
            dig=tot%10
            tot=tot//10  
            
            newnode = ListNode(dig)
            cur.next = newnode
            cur = newnode
            
        return ans


        