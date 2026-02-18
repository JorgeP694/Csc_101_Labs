#Name:
#Section:

import data

# Write your functions for each part in the space below.

# Part 1
'''Design Recipe (Write your design recipe here!)
input:a string 
output: the count of vowels in the string 
purpose:count how many vowles are in a string
Steps:
1) Start the counter @0
2)go through the string one character at a time
3)if the character is a vowel add 1 to the counter 
4)return counter 
'''
# Implementation
def vowel_count(s: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

# Part 2
'''Design Recipe (Write your design recipe here!)
input: list of list of integers
output: list of list of integers
purpose: From a list of lists of ints, keep only the nested lists that have length 3 or more.
Steps:
1) create empty list
2)go through each nested list in the imput
3)if its len is at least 3 add to result
4)result list
'''
# Implementation
def long_lists(lists: list[list[int]]) -> list[list[int]]:
    result: list[list[int]] = []
    for sub in lists:
        if len(sub) >= 3:
            result.append(sub)
    return result

# Part 3
'''Design Recipe (Write your design recipe here!)
input: list of list of integers
output: list of list of int
purpose: crate list of list where the lested list has a len of 2 are put into decending order averything else stays the same. 
Steps:
1) create empty list 
2)go through each nested list in the imput
3)if its len is at least 2 
    3.a) if first number is smaller than second swap them
    3.b)or leave as is
4)if the nested list is not length 2 copy it as-is
5)add the new results to the reslut
6)return the result 
'''
# Implementation
def decending_pairs(lists: list[list[int]]) -> list[list[int]]:
    result: list[list[int]] = []
    for sub in lists:
        if len(sub) == 2:
            a, b = sub[0], sub[1]
            if a < b:
                result.append([b, a])
            else:
                result.append([a, b])
        else:
            result.append(list(sub))
    return result

# Part 4
'''Design Recipe (Write your design recipe here!)
input: price 1 & 2
output: total price
purpose:add the price of 2 things where the cents is never above 99
Steps:
1) add the dollars together
2)add the cents together 
3) if cents is 100 or more
    3.a)conver extra cents into dollars 
    3.b)keep left over cents
4)return new price dollars and cents 
'''
# Implementation
def add_prices(p1: data.Price, p2: data.Price) -> data.Price:
    total_cents = p1.cents + p2.cents
    carry_dollars = total_cents // 100
    cents = total_cents % 100
    dollars = p1.dollars + p2.dollars + carry_dollars
    return data.Price(dollars, cents)


# Part 5
'''Design Recipe (Write your design recipe here!)
input:a rectangle
output:a number representing the perimitar
purpose: find the perimiter of an axis aligned rectangle given by top-left and bottom-right points.
Steps:
1)Compute the width = (bottom_right.x − top_left.x).
2)Compute the height = (top_left.y − bottom_right.y).
3)Perimeter = 2 × (width + height).
4)Return the perimeter.
'''
# Implementation
def rectangle_perimeter(rect: data.Rectangle) -> float:
    width = rect.bottom_right.x - rect.top_left.x
    height = rect.top_left.y - rect.bottom_right.y
    return 2 * (width + height)

# Part 6
'''Design Recipe (Write your design recipe here!)
input: list of floats
output: list of floats 
purpose: return only points in the third quadrent
Steps:
1)create empty list
2)go through each poin in the imput list
3)if x and y are negative add it to the result
4)return list
'''
# Implementation
def are_in_negative_quadrant(points: list[data.Point]) -> list[data.Point]:
    result: list[data.Point] = []
    for p in points:
        if p.x < 0 and p.y < 0:
            result.append(p)
    return result


# Part 7
'''Design Recipe (Write your design recipe here!)
input:a rectangle 
output:a circle
purpose: return the smallest circle that fully encloses the rectangle 
Steps:
1)find the center of the rectangle
    1.a)average x values
    1.b)average y values
2)pick a corner of any rectangle
3)compute the distance from center to the corner
4) return new circle
'''
# Implementation
def circle_bound(rect: data.Rectangle) -> data.Circle:
    tl = rect.top_left
    br = rect.bottom_right

    center_x = (tl.x + br.x) / 2
    center_y = (tl.y + br.y) / 2
    center = data.Point(center_x, center_y)

    radius = ((tl.x - center_x) ** 2 + (tl.y - center_y) ** 2) ** 0.5
    return data.Circle(center, radius)


# Part 8
'''Design Recipe (Write your design recipe here!)
input: a list of employee pay
output: a list of strings representing the employee name
purpose: give name of emploees who earn more than the average 
Steps:
1)if list is empty return empty list
2)add up all pay rates
3)compute the average pay
4)go through the list collect name of employees who are abouve average
5)return the list of names 
'''
# Implementation
def higher_than_average(employees: list[data.Employee]) -> list[str]:
    if len(employees) == 0:
        return []

    total = 0
    for e in employees:
        total += e.pay_rate
    avg = total / len(employees)

    result: list[str] = []
    for e in employees:
        if e.pay_rate > avg:
            result.append(e.name)
    return result
