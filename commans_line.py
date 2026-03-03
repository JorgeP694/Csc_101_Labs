#task 3
import sys
from convert import str_to_float

"""
   Purpose: Convert command-line arguments to floats and return their sum.
   Input: list of strings (command-line arguments)
   Output: float (sum of valid float conversions)
   """
def command_line_arguments(args: list[str]) -> float:
    total = 0.0
    for arg in args:
        value = str_to_float(arg)
        if value is not None:
            total += value
    return total





if __name__ == "__main__":
    # sys.argv[0] is the program name
    arguments = sys.argv[1:]
    total = command_line_arguments(arguments)
    print(total)