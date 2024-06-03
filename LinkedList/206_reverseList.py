from typing import List

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def reverseList(self,head:ListNode)->ListNode:
        if head==None or head.next==None:
            return head

        cur = self.reverseList(head.next)
        head.next.next=head

        head.next = None

        return cur

#创建链表
def createLinkedList(nums:List[int])->ListNode:
    if nums==None:
        return None
    head = ListNode(nums[0])
    cur = head
    for num in nums[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    return head

#打印链表
def printLinkedList(head:ListNode):
    cur = head
    while cur!= None:
        print(cur.value, end = "->")
        cur = cur.next
    print("None")

if __name__ == "__main__":
    # 提示用户输入一串数字，用空格分隔
    input_str = input("请输入一串数字，用空格分隔: ")
    # 使用split()方法将输入字符串分割成一个列表
    nums = [int(num) for num in input_str.split()]
    head = createLinkedList(nums)
    print("原始链表：")
    printLinkedList(head)
    solution = Solution()
    reversed_head = solution.reverseList(head)
    print("\n翻转后的链表：")
    printLinkedList(reversed_head)
