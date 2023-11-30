from Largest_submatrix_with_rearrangements import *
import random
import numpy as np

class Node:
    def __init__(self, matrix, parent=None, swapped=None):
        self.matrix = matrix
        self.parent = parent
        self.swapped = swapped  # keep track of the swapped columns
        self.children = []
        self.wins = 0
        self.visits = 0

    def expand(self):
        n = len(self.matrix[0])
        i, j = random.sample(range(n), 2)  # select two random distinct columns
        if not self.is_swap_duplicate((i, j)):  # avoid swapping the same two columns twice
            new_matrix = self.matrix.copy()
            new_matrix[:, [i, j]] = new_matrix[:, [j, i]]  # swap columns i and j
            self.children.append(Node(new_matrix, parent=self, swapped=(i, j)))

    def is_swap_duplicate(self, swap):
        node = self
        while node is not None:
            if node.swapped == swap:
                return True
            node = node.parent
        return False

    def simulate(self):
        return eval_matrix(self.matrix)

    def update(self, result):
        self.visits += 1
        self.wins += result

    def is_fully_expanded(self):
        return len(self.children) > 0

    def best_child(self):
        return max(self.children, key=lambda c: c.wins/c.visits)

def monte_carlo_tree_search(root, iterations, max_depth):
    for _ in range(iterations):
        node = root
        depth = 0
        # Selection
        while node.is_fully_expanded() and depth < max_depth:
            node = node.best_child()
            depth += 1
        # Expansion
        node.expand()
        # Simulation
        for child in node.children:
            result = child.simulate()
            # Backpropagation
            child.update(result)
            node.update(result)
    return root.best_child().matrix

def largest_submatrix_mcts(matrix):
    """
    This function returns the area of the largest sub-matrix with all ones.
    It takes as input a binary matrix.
    If the matrix is empty or the first row is empty, it returns 0.
    Otherwise, it generates all possible matrices with permuted columns.
    Then, it evaluates the area of the largest sub-matrix for each permuted matrix and returns the maximum area found.
    """
    if not matrix or not matrix[0]:
        return 0

    root = Node(matrix)
    best_matrix = monte_carlo_tree_search(root, 1000, 50)
    return eval_matrix(best_matrix)