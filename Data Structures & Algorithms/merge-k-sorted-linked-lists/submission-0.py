# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists and len(lists) == 0:
            return None

        while len(lists) > 1:
            MergedLists = []

            for i in range(0, len(lists), 2):
                A = lists[i]
                B = lists[i + 1] if i + 1 < len(lists) else None
                MergedLists.append(self.MergeTwo(A, B))
            
            lists = MergedLists

        return lists[0]

    def MergeTwo(self, A, B):
        temp = ListNode(-1)
        dummy = temp
        
        while A and B:
            if A.val <= B.val:
                dummy.next = A
                A = A.next
            else:
                dummy.next = B
                B = B.next
            dummy = dummy.next
        
        if A:
            dummy.next = A
        else:
            dummy.next = B

        return temp.next