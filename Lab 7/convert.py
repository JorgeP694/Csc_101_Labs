# task 1

'''
Purpose: convert string to float
Input: single paramiter string
Output: float unlest not possible it will return none
Implimitation:
'''

def str_to_float(input: str) -> float:
    try:
        return float(input)
    except ValueError:
        return None
    except TypeError:
        return None


