from convert import str_to_float

'''
input: person inputs while running
output: tally of numbers lst[float]
purpose:Read numbers from the keyboard until the user types "done", /
     convert valid inputs to floats, and return a list of those floats.
'''

def gather_numbers() -> list[float]:
    numbers: list[float] = []
    while True:
        text = input("Enter a number (or 'done'): ").strip()
        if text == "done":
            break
        value = str_to_float(text)
        if value is not None:
            numbers.append(value)
    return numbers

if __name__ == "__main__":
    nums = gather_numbers()
    print(sum(nums))