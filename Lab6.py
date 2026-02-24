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
def selection_sort_books(books: list[Book]) -> None:
    for i in range(len(books) - 1):
        min_index = i
        for j in range(i + 1, len(books)):
            if books[j].title < books[min_index].title:
                min_index = j
        temp = books[i]
        books[i] = books[min_index]
        books[min_index] = temp

# Part 2
# input:single peramiter string
# output: returns a string where lowercase letters become uppercase and uppercase become lowercase
# purpose: swap upper and lowercase letters
# example: def swap_case ['Hi There This is an Example'] -> 'hI tHERE tHis IS AN eXAMPLE'
# implementation:
def swap_case(s: str) -> str:
    result = ""
    for ch in s:
        if ch.islower():
            result += ch.upper()
        elif ch.isupper():
            result += ch.lower()
        else:
            result += ch
    return result

# Part 3
# input: put in a string with and a letter that you want replaiced with another
# output:string where letters are that were stated swaped with the other letters
# purpose: Return a new string where every occurrence of old is replaced with new.
# example:str_translate('abcdcba', 'a', 'x') -> 'xbcdcbx'
# implementation:
def str_translate(s: str, old: str, new: str) -> str:
    result = ""
    for ch in s:
        if ch == old:
            result += new
        else:
            result += ch
    return result

# Part 4
# input: s(str)
# output:dict[str, int] mapping word -> count
# purpose:Count space-delimited words in a string.
# example:histogram('a b a a') -> {'a': 3, 'b': 1}
# implementation:
def histogram(s: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    words = s.split()
    for w in words:
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1
    return counts

