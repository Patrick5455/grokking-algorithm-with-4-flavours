import algoexpert.easy.validate_subsequence as vs
import unittest


class ValidateSubSequenceUnitTest(unittest.TestCase):
    def test_is_valid_subsequence(self):
        print("valid subsequence test cases")
        counter = 1
        for test_input in valid_subsequence_test_inputs:
            print(f"testing case {counter}")
            self.assertTrue(
                vs.is_valid_subsequence_solution(test_input['array'], test_input['sequence']))
            counter += 1

    def test_is_invalid_subsequence(self):
        print("\n\n invalid subsequence test cases")
        counter = 1
        for test_input in invalid_subsequence_test_inputs:
            print(f"testing case {counter}")
            self.assertFalse(
                vs.is_valid_subsequence_solution(test_input['array'], test_input['sequence']))
            counter += 1


valid_subsequence_test_inputs = [
    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [1, 6, -1, 10]
    },

    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [5, 1, 22, 25, 6, -1, 8, 10]
    },

    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [5, 1, 22, 6, -1, 8, 10]
    },

    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [22, 25, 6]
    },

    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [1, 6, 10]
    },

    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [5, 1, 22, 10]
    },

    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [5, -1, 8, 10]
    },

    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [25]
    },

    {
        "array": [1, 1, 1, 1, 1],
        "sequence": [1, 1, 1]
    }

    ]

invalid_subsequence_test_inputs = [

    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [5, 1, 22, 25, 6, -1, 8, 10, 12]
    },

    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [4, 5, 1, 22, 25, 6, -1, 8, 10]
    },

    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [5, 1, 22, 23, 6, -1, 8, 10]
    },

    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [5, 1, 22, 22, 25, 6, -1, 8, 10]
    },

    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [5, 1, 22, 22, 6, -1, 8, 10]
    },

    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [1, 6, -1, -1]
    },

    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [1, 6, -1, -1, 10]
    },

    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [1, 6, -1, -2]
    },

    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [26]
    },

    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [5, 1, 25, 22, 6, -1, 8, 10]
    },

    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [5, 26, 22, 8]
    },

    {
        "array": [1, 1, 6, 1],
        "sequence": [1, 1, 1, 6]
    },

    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [1, 6, -1, 10, 11, 11, 11, 11]
    },

    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [5, 1, 22, 25, 6, -1, 8, 10, 10]
    },

    {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [1, 6, -1, 5]
    }

]
