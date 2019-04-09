class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, node):
        """
        this functions adds a new node to the existing list at the start
        :param node:
        :return:
        """
        new_node = Node(node)
        new_node.next = self.head
        self.head = new_node

    def reverselist(self):
        """
        this function reverses the linked list but it has a bug
        :return:
        """
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        # the below line is missing. With out this we return only the original
        # head element. I added the below line to run my test cases
        self.head = prev
        return self.head

"""
1. Q: Please correct the defect in reverseList so it reverses a linked-list correctly.
   A: All is good until last step...The code should attach previous as head which is missing.

2. Q: How would you test reverseList? What specific functional test cases would you try?
   A: 1) Trying to reverse an empty linked list
      2) Trying to reverse an linked list with duplicate values
      3) Some memory tests if the size of linked list is too large.

3. Q: Implement 2 test cases from 2) in the language/scripting of your choice.
   A: Please find the below test cases.
"""

"""Test cases for reversing a linked list"""

import  unittest

class TestReverseLinkedList(unittest.TestCase):
    """Test case suite for Reverse LinkedList"""

    @classmethod
    def setUpClass(cls):
        print("Setting up the test class data...")
        cls.linked_list = LinkedList()

    @classmethod
    def tearDownClass(cls):
        print("Teardown the test data")

    def test_01_empty_linked_list(self):
        head_of_reversed_linked_list = self.linked_list.reverselist()
        self.assertEqual(head_of_reversed_linked_list, None)

    def test_02_positive_test_case_with_duplicates(self):
        """this test case covers two scenarios..."""
        self.linked_list.add_node(3)
        self.linked_list.add_node(5)
        self.linked_list.add_node(5)
        self.linked_list.add_node(10)
        # original linked list: 10 -> 5 -> 5 -> 3
        head_of_reversed_linked_list = self.linked_list.reverselist()
        # reversed: 3 -> 5 - > 5 -> 10
        self.assertEqual(head_of_reversed_linked_list.data, 3)

if __name__ == "__main__":
   unittest.main()


