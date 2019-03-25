class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverselist(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        #self.head = prev -this is the bug . This line is missing
        return head

"""
1. Q: Please correct the defect in reverseList so it reverses a linked-list correctly.
   A: All is good until last step...The code should attach previous as head which is missing.

2. Q: How would you test reverseList? What specific functional test cases would you try?
   A: Will implement tomorrow

3. Q: Implement 2 test cases from 2) in the language/scripting of your choice.
   A: Will implement tomorrow
"""

