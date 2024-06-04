from LinkedList.reverseList import *

class Solution:
    def partition(self, head:ListNode, x: int) -> ListNode:

        bigHead = ListNode(0)
        bigTail = bigHead

        smallHead = ListNode(0)
        smallTail = smallHead

        while head is not  None:
            if head.value < x:
                smallTail.next = head
                smallTail = smallTail.next
            else:
                bigTail.next = head
                bigTail = bigTail.next
            head = head.next

        smallTail.next = bigHead.next
        bigTail.next = None

        return smallHead.next

if __name__ == '__main__':
    input_str = input("请输入一串数字，用空格分隔: ")
    # 使用split()方法将输入字符串分割成一个列表
    nums = [int(num) for num in input_str.split()]
    head = createLinkedList(nums)
    input_x = input("请输入数字x：")
    x = int(input_x)

    node =Solution().partition(head, x)
    printLinkedList(node)



