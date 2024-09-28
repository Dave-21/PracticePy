# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
 #def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        iterator = head
        listLength = 0
        counter = 0
        prev = None

        # Count elements
        while iterator:
            listLength += 1
            iterator = iterator.next
        elementToRemove = listLength - n
        
        # Base case
        if elementToRemove < 1:
            return head.next

        iterator = head
        while iterator:
            if counter == (elementToRemove-1):
                prev = iterator
            elif counter == elementToRemove:
                prev.next = iterator.next
                break
            counter += 1
            iterator = iterator.next

        return head

sol = Solution()
nodes = ListNode([1,2,3,4,5])
results = sol.removeNthFromEnd(nodes, 2)

iterator = results
while iterator:
    print(iterator.val)
    iterator = iterator.next