from LinkedList.reverseList import *

class Solution:
    def getIntersectionNode(self, headA:ListNode, headB:ListNode)->ListNode:
        if(headA==None or headB==None):
            return None

        pointerA = headA
        pointerB = headB
        while pointerA!=pointerB:
            if pointerA == None:
                pointerA = headB
            else:
                pointerA=pointerA.next
            if pointerB == None:
                pointerB = headA
            else:
                pointerB=pointerB.next

        return pointerA

if __name__ == "__main__":
    #创建链表A
    nums = [1,2,3,5,6,7]
    headA = createLinkedList(nums)

    node9 = ListNode(9)
    node8 = ListNode(8)
    node9.next = node8
    node8.next = headA.next.next.next

    #创建链表B
    headB = node9

    #找到相交链表
    intersection_node = Solution().getIntersectionNode(headA, headB)

    if intersection_node:
        print("两个链表相交于节点值为", intersection_node.value)
    else:
        print("两个链表不相交")





