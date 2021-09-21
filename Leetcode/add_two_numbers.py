"""
Problem statement:

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        n1 = l1
        n2 = l2
        next_node = None
        carry = 0
        while not (n1 is None and n2 is None and not carry):
            v1 = n1.val if not n1 is None else 0
            v2 = n2.val if not n2 is None else 0
            digit_sum = v1 + v2 + carry
            if next_node is None:
                next_node = ListNode(int(digit_sum % 10), None)
                return_node = next_node
            else:
                next_node.next = ListNode(int(digit_sum % 10), None)
                next_node = next_node.next
            carry = (digit_sum - next_node.val) / 10
            n1 = n1.next if not n1 is None else None
            n2 = n2.next if not n2 is None else None
         
        return return_node


def test(list1, list2):
    """
    Function to test solution; lists will be converted to linked lists.
    Result will be printed.

    Args:
        list1 (list)
        list2 (list)
    """

    linkedlist1 = None
    while len(list1):    
        linkedlist1 = ListNode(list1.pop(0), linkedlist1)
    
    linkedlist2 = None
    while len(list2):    
        linkedlist2 = ListNode(list2.pop(0), linkedlist2)
    
    sol = Solution()
    out = sol.addTwoNumbers(linkedlist1, linkedlist2)
    outlist = []
    while not out is None:
        outlist.append(out.val)
        out = out.next
    print(outlist)
		
