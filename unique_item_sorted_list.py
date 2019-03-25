class MyArrayProcessing:
    def  whatAmIdoing(self,input):
        j = 0
        i = 1
        if len(input) < 2:
            return input

        while (i<len(input)):
            if (input[i]==input[j]):
                i+=1
            else:
                j += 1
                input[j] = input[i]
                i += 1

        return  input[:j+1]

obj = MyArrayProcessing()
print(obj.whatAmIdoing([2,3,3,4,5,5,5,6]))


"""
Note: As I am familirar with Python at this point...I converted code to Python for faster implementation

1. Q: What is the "whatAmIdoing" method doing (input is assumed to be sorted)?
   A: Extracting unique items from a sorted list

2. Q: How would you test "whatAmIDoing?" What specific functional test cases would you try?
   A: Will update 

3. Q: Implement 2 test cases from 2) in the language/scripting of your choice.
   A:  Will update

"""



import unittest
class TestMyArrayProcessing(unittest.Testcase):
    # TODO: test cases yet to be implemented
    pass