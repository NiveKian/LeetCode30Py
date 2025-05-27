# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# ListNode = ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}}

class Solution:

    def valFromSLList(self, graph: Optional[ListNode]) -> int:
        if graph.next:
            nval = self.valFromSLList(graph.next)
            return int(str(nval) + str(graph.val))
        else:
            return graph.val

    def newLinkListByInt(self, val: int) -> Optional[ListNode]:
        sval = str(val)
        if len(sval) != 1:
            return ListNode(int(sval[-1]), self.newLinkListByInt(int(sval[:-1])))
        else:
            return ListNode(int(sval[-1]))

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = self.valFromSLList(l1)
        val2 = self.valFromSLList(l2)
        result = val1 + val2

        return self.newLinkListByInt(result)
        