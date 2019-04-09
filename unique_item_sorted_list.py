class MyArrayProcessing:
    def  whatAmIdoing(self,input):
        """
        Assumption: a list of sorted integers

        :param input (list): a list with integers
        :return:
        """
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
print("\n\n")


"""
Note: As I am familirar with Python at this point...I converted code to Python for faster implementation

1. Q: What is the "whatAmIdoing" method doing (input is assumed to be sorted)?
   A: Extracting unique items from a sorted list

2. Q: How would you test "whatAmIDoing?" What specific functional test cases would you try?
   A: My goal is to test all cases that touch all parts of the code
      1) Four test cases where length of the input list is 0, 1, 2, 3. This
         makes sure the boundary conditions are covered.
      2) Test cases where list has negative values
      3) test cases where list has decimal values
      4) test cases where list has combination of negative, positive and 
      decimal values
      5) Alternate test cases, where large integers and maximum list size 
      can also be covered.

3. Q: Implement 2 test cases from 2) in the language/scripting of your choice.
   A:  Please find below test cases

"""

"""
Test cases
"""

import unittest

class TestMyArrayProcessing(unittest.TestCase):
    """Test Case class for MyArrayProcessing"""
    @classmethod
    def setUpClass(cls):
        print("Setting up class data\n")
        cls.class_obj = MyArrayProcessing()

    @classmethod
    def tearDownClass(cls):
        print("Tearing down class\n")

    def test_01_empty_list(self):
        test_data = []
        output = self.class_obj.whatAmIdoing(test_data)
        self.assertEqual(output, [])

    def test_02_all_list_elements_equal(self):
        test_data = [1,1,1,1,1,1,1,1,1,1]
        output = self.class_obj.whatAmIdoing(test_data)
        self.assertListEqual(output, [1])

    def test_03_all_unique_elements_equal(self):
        test_data = [1,2,3,4,5,6,7,8]
        output = self.class_obj.whatAmIdoing(test_data)
        self.assertListEqual(output, test_data)

    def test_04_all_negative_elements(self):
        test_data = [-3,-3,-2,-1]
        output = self.class_obj.whatAmIdoing(test_data)
        self.assertListEqual(output, [-3,-2,-1])

    def test_05_some_positive_and_negative_elements(self):
        test_data = [-3,-1,-1,5,10,10]
        output = self.class_obj.whatAmIdoing(test_data)
        self.assertListEqual(output, [-3, -1, 5, 10])

    def test_06_decimal_values(self):
        test_data = [-4.5,-4.5,1, 5.4,5.4, 10]
        output = self.class_obj.whatAmIdoing(test_data)
        self.assertListEqual(output, [-4.5, 1, 5.4, 10])

if __name__ == "__main__":
    unittest.main()

