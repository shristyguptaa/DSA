# Convert Binary Number in a Linked List to Integer

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        num = 0
        while head is not None:
            num = num * 2 + head.val
            head = head.next
        return num
