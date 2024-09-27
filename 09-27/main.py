# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        iterator = head
        listLength = 0
        while iterator:
            listLength += 1
            iterator = iterator.next

        elementToRemove = listLength - n

        counter = 0

        iterator = head
        prev = None
        while iterator:
            if counter == (elementToRemove-1):
                prev = iterator
            elif counter == (elementToRemove+1):
                prev.next = iterator
            counter += 1
            iterator = iterator.next

        return head