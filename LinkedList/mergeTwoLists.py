from LinkedList.reverseList import *

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1, cur2 = l1, l2
        head = ListNode(0)
        node = head
        while cur1 and cur2:
            if cur1.value < cur2.value:
                node.next = cur1
                cur1 = cur1.next
            else:
                node.next = cur2
                cur2 = cur2.next
            node = node.next

        if cur1 is None:
            node.next = cur2
        if cur2 is None:
            node.next = cur1
        return head.next

if __name__ == "__main__":
    input_str1 = input("请输入第一个链表，用空格隔开：")
    nums1 = [int(num) for num in input_str1.split()]
    headA = createLinkedList(nums1)
    input_str2 = input("请输入第二个链表，用空格隔开：")
    nums2 = [int(num) for num in input_str2.split()]
    headB = createLinkedList(nums2)

    node = Solution().mergeTwoLists(headA, headB)

    printLinkedList(node)