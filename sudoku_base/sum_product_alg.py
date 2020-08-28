""" This module provides the necessary methods for calculating the elements of the sudoku frame
based on the sum-product-algorithm."""

# imports
import numpy as np
from sudoku_base.sudoku_frame import SudokuFrame


def initialize_probs(frame: SudokuFrame = None):
    probs = np.zeros(shape=frame.matrix.shape)

# # I think this function is not needed. 
    # indexes = np.where(frame.matrix == 0)
    # print(indexes)
    # [x + 1 if element==0 else x + 5 for element in frame.matrix]


    return probs


frame = SudokuFrame(3, 3)
SudokuFrame.set_field_value(frame, index=(1, 1), value=7)
SudokuFrame.set_field_value(frame, index=(2, 1), value=3)
SudokuFrame.set_field_value(frame, index=(0, 0), value=1)
print(frame.matrix)
print(initialize_probs(frame))
