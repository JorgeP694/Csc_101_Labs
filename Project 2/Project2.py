
#Name:
#Section: 
import classes

# Write your functions for each part in the space below.

# Part 1
'''Design Recipe (Write your design recipe here!)
input: two Point objects
output: Rectangle object
purpose: Create rectangle from any two opposite points
Steps:
1) Extract x and y from both points.
2) Determine min and max x values.
3) Determine min and max y values.
4) Top-left uses min x and max y.
5) Bottom-right uses max x and min y.
6) Return Rectangle with those points.
'''
# Implementation
def create_rectangle(p1: classes.Point, p2: classes.Point) -> classes.Rectangle:
    min_x = min(p1.x, p2.x)
    max_x = max(p1.x, p2.x)
    min_y = min(p1.y, p2.y)
    max_y = max(p1.y, p2.y)

    top_left = classes.Point(min_x, max_y)
    bottom_right = classes.Point(max_x, min_y)

    return classes.Rectangle(top_left, bottom_right)

# Part 2
'''Design Recipe (Write your design recipe here!)
input: two Duration objects
output: boolean
purpose: Determine if first duration is shorter
Steps:
1) Convert both durations to total seconds.
2) Compare first total to second total.
3) Return True if first is smaller.
'''
# Implementation
def shorter_duration_than(d1: classes.Duration, d2: classes.Duration) -> bool:
    total1 = d1.minutes * 60 + d1.seconds
    total2 = d2.minutes * 60 + d2.seconds
    return total1 < total2

# Part 3
'''Design Recipe (Write your design recipe here!)
input: list of Song, Duration upper bound
output: list of Song
purpose: Filter songs shorter than given duration
Steps:
1) Initialize empty result list.
2) For each song in list:
3) If song duration shorter than bound:
4) Append song to result.
5) Return result list.
'''
# Implementation
def songs_shorter_than(songs: list[classes.Song], max_duration: classes.Duration) -> list[classes.Song]:
    result = []
    for song in songs:
        if shorter_duration_than(song.duration, max_duration):
            result.append(song)
    return result


# Part 4
'''Design Recipe (Write your design recipe here!)
input: list of Song, list of indices
output: Duration object
purpose: Compute total running time of playlist
Steps:
1) Initialize total seconds to zero.
2) For each index in playlist:
3) If index valid (0 ≤ index < len list):
4) Add song duration in seconds to total.
5) Convert total seconds to minutes and seconds.
6) Return Duration with normalized values.
'''
# Implementation
def running_time(songs: list[classes.Song], playlist: list[int]) -> classes.Duration:
    total_seconds = 0
    for index in playlist:
        if 0 <= index < len(songs):
            song = songs[index]
            total_seconds += song.duration.minutes * 60
            total_seconds += song.duration.seconds
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return classes.Duration(minutes, seconds)


# Part 5
'''Design Recipe (Write your design recipe here!)
input: list of city links, route list
output: boolean
purpose: Validate route connectivity between cities
Steps:
1) If route length ≤ 1 return True.
2) For each consecutive city pair:
3) Check if link exists in either order.
4) If no link found return False.
5) If all links valid return True.
'''
# Implementation
def validate_route(city_links: list[list[str]], route: list[str]) -> bool:
    if len(route) <= 1:
        return True
    for i in range(len(route) - 1):
        city1 = route[i]
        city2 = route[i + 1]
        link_found = False
        for link in city_links:
            if (city1 in link) and (city2 in link):
                link_found = True
                break
        if not link_found:
            return False
    return True

# Part 6
'''Design Recipe (Write your design recipe here!)
input: list of integers
output: Optional[int]
purpose: Find start index of longest contiguous repetition
Steps:
1) If list empty return None.
2) Track current value and run length.
3) Track max length and starting index.
4) Iterate through list comparing neighbors.
5) Update max when longer run found.
6) Return starting index of longest run.
'''
# Implementation
def longest_repetition(values: list[int]) -> int | None:
    if not values:
        return None
    max_length = 1
    max_start = 0
    current_length = 1
    current_start = 0
    for i in range(1, len(values)):
        if values[i] == values[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_start = current_start
            current_length = 1
            current_start = i
    if current_length > max_length:
        max_start = current_start
    return max_start
