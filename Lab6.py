# Name:
# Section: 7
from book_class import *
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        # SWAPPING
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
# input: list of book title
# output:a sorted list by title in alphabetical order
# purpose: sort book title bames
# example: def selection_sort_books [lst[book9, book2, book7] -> lst[book2, book,7 book9]
# implementation: 


# Part 2
# input:single peramiter string
# output: returns a string where lowercase letters become uppercase and uppercase become lowercase
# purpose: swap upper and lowercase letters
# example: def swap_case ['Hi There This is an Example'] -> 'hI tHERE tHis IS AN eXAMPLE'
# implementation:

# Part 3
# input: put in a string with and a letter that you want replaiced with another
# output:string where letters are that were stated swaped with the other letters
# purpose:
# example:
# implementation:

# Part 4
# input:
# output:
# purpose:
# example:
# implementation:


