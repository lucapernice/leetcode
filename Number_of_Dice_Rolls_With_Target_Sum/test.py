import unittest
from number_of_dice_to_roll import numRollsToTarget

class TestNumRollsToTarget(unittest.TestCase):

    def test_numRollsToTarget(self):
        # Test case 1
        n = 3
        k = 6
        target = 7
        expected_output = 15
        result = numRollsToTarget(n=n, k=k, target=target)
        self.assertEqual(result, expected_output)

    def test_numRollsToTarget_2(self):
        # Test case 2
        n = 2
        k = 6
        target = 10
        expected_output = 3
        self.assertEqual(numRollsToTarget(n=n, k=k, target=target), expected_output)

    def test_numRollsToTarget_3(self):
        # Test case 3
        n = 1
        k = 6
        target = 3
        expected_output = 1
        self.assertEqual(numRollsToTarget(n=n, k=k, target=target), expected_output)



        # Add more test cases as needed

if __name__ == "__main__":
    unittest.main()
