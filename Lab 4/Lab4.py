# Lab 4
# Your name: Jorge Preciado
# Your Section:-9


# Write your functions for each part in the space below.

# Task 1 - last_element
# input: list of a list of the float
# output: the last value in a list of the float
# purpose: create a list of list with the final value of each list.
# example: last_element[[4,7,9],[2.3,4.5]] -> [9,4.5]
'''
    steps:
        1.create an empty list
        2. go through each inner list
        3.ignore epty list
        4. take the idx[-1]
        5.add last val to new list
        5. return list
'''

def last_element(input: list[list[float]]) -> list[float]:
    non_empty = []
    for lst in input:
        if len(lst) != 0:
            non_empty.append(lst)

    result = []
    for lst in non_empty:
        result.append(lst[len(lst) - 1])

    return result

# Task 2 - pass_fail
# input: list of list of int
# output: a list of strings (pass or fail)
# purpose:decied if each student passes or fails based on grade
# example:pass_fail([[90,95],[30,70]], 65) -> ["Pass","fail"]
'''
    steps:
    1. create an empty list for results
    2. look at one student’s grades at a time
    3. check if all grades are above the threshold
    4. if yes, add "pass" to the result list
    5. if not, add "fail" to the result list
    6. return the result list
    '''
def pass_fail(grades: list[list[int]], threshold: int) -> list[str]:
    result = []
    for student_grades in grades:
        passed = True
        for grade in student_grades:
            if grade <= threshold:
                passed = False
        if passed:
            result.append("pass")
        else:
            result.append("fail")
    return result

# Task 3 - search_value
# input: a list of values and a value to look for
# output: a string ("Found" or "Not Found")
# purpose: check if a value exists in the list
# example: search_value([1, 2, 3], 2) -> "Found"
'''
    steps:
    1. go through each value in the list
    2. compare each value to the target value
    3. if a match is found, return "Found"
    4. if no match is found after checking everything, return "Not Found
"'''
def search_value(values: list, target) -> str:
    for item in values:
        if item == target:
            return "Found"
    return "Not Found"

# Task 4 - search_any
# input: a list of values and a value to look for
# output: a boolean (True or False)
# purpose: check whether a value appears in the list
# example: search_any([10, 20, 30], 20) -> True
'''
    steps:
    1. go through each value in the list
    2. compare it to the target value
    3. if a match is found, return True
    4. if no match is found, return False
'''
def search_any(values: list, target) -> bool:
    for item in values:
        if item == target:
            return True
    return False

# Task 5 - reverse_value
# input: a list or a string
# output: the same list or string reversed
# purpose: reverse the order of elements without using built-in reverse tools
# example: reverse_value([1, 2, 3]) -> [3, 2, 1]
'''
    steps:
    1. create an empty result of the same type (list or string)
    2. start from the last position
    3. add each element to the result one by one
    4. move backward until the beginning is reached
    5. return the reversed result
'''
def reverse_value(value):
    result = value[:0]   # empty list or empty string
    i = len(value) - 1
    while i >= 0:
        if type(value)==list:
            result +=[value[i]]
        else:
            result += value[i]
        i -= 1
    return result


