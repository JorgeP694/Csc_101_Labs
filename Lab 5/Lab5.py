# Name:
# Section: 6 Due 2/13/26
#########################################################
import math
from unittest import result

import data

# Write your functions for each part in the space below.
# Task 1
''' Design Receipe
input:list[points]
output:a list containing the x coord of each point 
purpose:to find the x cord of each point
Steps:
1.create new list 
2.take points in list 
3 identify x append to new list 
4.if point dosent have x coord move to nect given point
5.return new list 
'''
def x_coord(points: list[data.Point] )-> list[float]:
    new_list = []
    for point in points:
        new_list.append(point.x)
    return new_list


# Task 2
''' Design Receipe
input: list with point
output: returns all posotive x and y coords 
purpose: find points in the first quadernt of the Cartesian plane.
Steps:
1. create new list 
2. take points in list 
3. find if x is posotive
4. find if x is posotive 
5.if both positeive return point/
if not remove 
6. return new list

'''
def are_in_positive_quadrant(points: list[data.Point]) -> list[data.point]:
    new_list = []
    for point in points:
        if point.x and point.y:
            point = [point.x, point.y] >0
            append = new_list.append
        else:
            return new_list




# Task 3
''' Design Receipe
input:x and y from 2 diffrent points 
output:distance between x and y 
purpose:find the eucladian distnce 
Steps:
1.take point one
2.take point two
3.subtract x values 
4 subtract y values 
5. suare them
add the values together 
'''
def euclidean_distance(p1 : data.Point, p2 : data.Point) -> float:
    return math.sqrt((p2.x-p1.x)**2 + (p2.y-p1.y)**2)

# Task 4
''' Design Receipe
input: 2 diffrent points 
output: the manhattan distance between the two points 
purpose: find manhattan distance
Steps:
1.take point one
2.take point two
3.subtract x values 
4 subtract y values 
5. take the absolute value of both 
6.add them together 
7.return
'''
def manhattan_distance(p1 : data.Point, p2 : data.Point) -> float:
    return abs(p2.x-p1.x)+abs(p2.y-p1.y)
# Task 5
''' Design Receipe
input:list of points
output:list of distance from the origen 
purpose: to take list of points and take the distance of each and return them in a lsit 
Steps:
1. define origin 
2. take points in list 
3. take distance from origin 
'''
def distance_all(points: list[data.Point]) -> list[float]:
    origin = data.Point(0,0)
    result=[]
    for p in points:
        result.append(euclidean_distance(origin,p))
    return result
# Task 6
   # The function for Taks 6 should be within the class in data.py.


# Task 7
   # The function for Task 7 should be within the class in data.py.


# Task 8
''' Design Receipe
input: two time opbjects 
output: the time
purpose:add 2 times 
Steps:
1.add seconds
2.carry extra to minutes
3.add minutes
4.carry extra to hours
5.add hours
6.return new Time
'''
def time_add(t1: data.Time, t2: data.Time) -> data.Time:
    total_seconds = t1.second + t2.second
    carry_minutes = total_seconds // 60
    seconds = total_seconds % 60

    total_minutes = t1.minute + t2.minute + carry_minutes
    carry_hours = total_minutes // 60
    minutes = total_minutes % 60

    hours = t1.hour + t2.hour + carry_hours

    return data.Time(hours, minutes, seconds)

# Task 9
''' Design Receipe
input: list of floats
output:bool
purpose:check strictly descending order
Steps:
1.if list short return True
2.compare each pair
3.if not descending return False
4.return True
'''
def is_descending(values: list[float]) -> bool:
    if len(values) <= 1:
        return True

    for i in range(1, len(values)):
        if values[i] >= values[i - 1]:
            return False

    return True

# Task 10
''' Design Receipe
input:list of ints, lower index, upper index
output:int or None
purpose:find index of largest in range
Steps:
1.if lower greater than upper return None
2.adjust out of bounds indexes
3.search between indexes
4.track largest value
5.return its index
'''
def largest_between(values: list[int], lower: int, upper: int) -> int | None:
    if lower > upper:
        return None
    if not values:
        return None
    lower = max(0, lower)
    upper = min(len(values) - 1, upper)
    if lower > upper:
        return None
    largest_index = lower
    for i in range(lower, upper + 1):
        if values[i] > values[largest_index]:
            largest_index = i
    return largest_index

# Task 11
''' Design Receipe
input:list of Point objects
output:int or none
purpose:find index furthest from origin
Steps:
1.if list empty return None
2.compute distance for each point
3.find largest distance
4.return its index
'''
def furthest_from_origin(points: list[data.Point]) -> int | None:
    if not points:
        return None
    def distance_squared(p: data.Point) -> float:
        return p.x ** 2 + p.y ** 2
    largest_index = 0
    for i in range(1, len(points)):
        if distance_squared(points[i]) > distance_squared(points[largest_index]):
            largest_index = i
    return largest_index
