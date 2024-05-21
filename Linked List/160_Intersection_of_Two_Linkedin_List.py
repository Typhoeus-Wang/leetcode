# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        lenA, lenB = 0, 0

        cur = headA
        while cur:
            cur = cur.next
            lenA += 1

        cur = headB
        while cur:
            cur = cur.next
            lenB += 1

        curLong, curShort = headA, headB
        lenLong, lenShort = lenA, lenB
        
        if lenB > lenA:
            curLong, curShort = headB, headA
            lenLong, lenShort = lenB, lenA
        
        for i in range(lenLong - lenShort):
            curLong = curLong.next
        
        while curLong:
            if curLong == curShort:
                return curLong
            else:
                curLong = curLong.next
                curShort = curShort.next

        return None