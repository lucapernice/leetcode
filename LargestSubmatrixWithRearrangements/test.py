import unittest
from Largest_submatrix_with_rearrangements import consecutive_ones_row, consecutive_ones_col, all_permutations, matrix_column_permutation, eval_matrix, all_matrix_permutations


class MyTestCase(unittest.TestCase):
    def test_consecutive_ones_in_empty_row(self):
        result = consecutive_ones_row([[]], 0, 0)
        self.assertEqual(result, 0)

    def test_consecutive_ones_in_row_with_no_ones(self):
        result = consecutive_ones_row([[0, 0, 0]], 0, 0)
        self.assertEqual(result, 0)

    def test_consecutive_ones_in_row_with_all_ones(self):
        result = consecutive_ones_row([[1, 1, 1]], 0, 0)
        self.assertEqual(result, 3)

    def test_consecutive_ones_in_row_with_some_ones(self):
        result = consecutive_ones_row([[1, 1, 0, 1]], 0, 0)
        self.assertEqual(result, 2)

    def test_consecutive_ones_in_row_starting_from_middle(self):
        result = consecutive_ones_row([[0, 1, 1, 0]], 0, 1)
        self.assertEqual(result, 2)

    def test_consecutive_ones_in_empty_column(self):
        result = consecutive_ones_col([[]], 0, 0)
        self.assertEqual(result, 0)

    def test_consecutive_ones_in_column_with_no_ones(self):
        result = consecutive_ones_col([[0], [0], [0]], 0, 0)
        self.assertEqual(result, 0)

    def test_consecutive_ones_in_column_with_all_ones(self):
        result = consecutive_ones_col([[1], [1], [1]], 0, 0)
        self.assertEqual(result, 3)

    def test_consecutive_ones_in_column_with_some_ones(self):
        result = consecutive_ones_col([[1], [1], [0], [1]], 0, 0)
        self.assertEqual(result, 2)

    def test_consecutive_ones_in_column_starting_from_middle(self):
        result = consecutive_ones_col([[0], [1], [1], [0]], 1, 0)
        self.assertEqual(result, 2)

    def test_permutations_of_zero_elements(self):
        result = all_permutations(0)
        self.assertEqual(result, [[]])

    def test_permutations_of_single_element(self):
        result = all_permutations(1)
        self.assertEqual(sorted(result), sorted([[0]]))

    def test_permutations_of_two_elements(self):
        result = all_permutations(2)
        self.assertEqual(sorted(result), sorted([[0, 1], [1, 0]]))

    def test_permutations_of_three_elements(self):
        result = all_permutations(3)
        self.assertEqual(sorted(result), sorted([[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]))

    def test_matrix_permutation_with_empty_matrix(self):
        result = matrix_column_permutation([[]], [0])
        self.assertEqual(result, [[]])

    def test_matrix_permutation_with_single_column(self):
        result = matrix_column_permutation([[1], [2], [3]], [0])
        self.assertEqual(result, [[1], [2], [3]])

    def test_matrix_permutation_with_multiple_columns(self):
        result = matrix_column_permutation([[1, 2], [3, 4]], [1, 0])
        self.assertEqual(result, [[2, 1], [4, 3]])

    def test_matrix_permutation_with_invalid_permutation(self):
        with self.assertRaises(IndexError):
            matrix_column_permutation([[1, 2], [3, 4]], [2, 0])

    def test_eval_empty_matrix(self):
        result = eval_matrix([[]])
        self.assertEqual(result, 0)

    def test_eval_matrix_with_no_ones(self):
        result = eval_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.assertEqual(result, 0)

    def test_eval_matrix_with_all_ones(self):
        result = eval_matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        self.assertEqual(result, 9)

    def test_eval_matrix_with_some_ones(self):
        result = eval_matrix([[1, 1, 0], [1, 1, 0], [0, 0, 0]])
        self.assertEqual(result, 4)

    def test_eval_matrix_with_disconnected_ones(self):
        result = eval_matrix([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertEqual(result, 1)

    def test_matrix_permutations_with_empty_matrix(self):
        result = all_matrix_permutations([[]])
        self.assertEqual(result, [[]])

    def test_matrix_permutations_with_single_column(self):
        result = all_matrix_permutations([[1], [2], [3]])
        expected = [[[1], [2], [3]]]
        self.assertEqual(sorted(result), sorted(expected))

    def test_matrix_permutations_with_two_columns(self):
        result = all_matrix_permutations([[1, 2], [3, 4]])
        expected = [[[1, 2], [3, 4]], [[2, 1], [4, 3]]]
        self.assertEqual(sorted(result), sorted(expected))

    def test_matrix_permutations_with_three_columns(self):
        result = all_matrix_permutations([[1, 2, 3], [4, 5, 6]])
        expected = [
            [[1, 2, 3], [4, 5, 6]], [[1, 3, 2], [4, 6, 5]], [[2, 1, 3], [5, 4, 6]],
            [[2, 3, 1], [5, 6, 4]], [[3, 1, 2], [6, 4, 5]], [[3, 2, 1], [6, 5, 4]]
        ]
        self.assertEqual(sorted(result), sorted(expected))


if __name__ == '__main__':
    unittest.main()
