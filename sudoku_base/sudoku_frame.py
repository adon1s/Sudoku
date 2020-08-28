""" This module represents the actual sudoku frame. It implements the
sum-product-algorithm for solving the sudoku problem. """

# imports
import numpy as np


class SudokuFrame:
    """ Class for the sudoku frame."""
    def __init__(self, rows, clms):
        self.rows = rows
        self.clms = clms
        self.matrix = np.zeros((rows, clms))

    def set_field_value(self, index: (-1, -1), value: int = -1):
        self.matrix[index] = value

    def initialize_probs(self):
        probs = np.zeros(shape=self.matrix.shape)

        return probs


frame = SudokuFrame(3, 3)
#print(frame.matrix)
SudokuFrame.set_field_value(frame, index=(1, 1), value=7)
SudokuFrame.set_field_value(frame, index=(2, 1), value=3)
SudokuFrame.set_field_value(frame, index=(0, 0), value=1)

#print(frame.initialize_probs())

