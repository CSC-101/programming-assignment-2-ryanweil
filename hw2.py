from data import*

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(point1:Point,point2: Point)-> Rectangle:
#determine top_left and bottom_right points
    top_left_x = min(point1.x, point2.x)
    top_left_y = max(point1.y, point2.y)
    bottom_right_x = max(point1.x, point2.x)
    bottom_right_y = min(point1.y, point2.y)

    #create points for the rectangle
    top_left=Point(top_left_x, top_left_y)
    bottom_right=Point(bottom_right_x, bottom_right_y)

    return Rectangle(top_left, bottom_right)

# Part 2

def shorter_duration_than(duration1: Duration, duration2: Duration) -> bool:
    # Convert each duration to total seconds for comparison
    total_seconds1 = duration1.minutes * 60 + duration1.seconds
    total_seconds2 = duration2.minutes * 60 + duration2.seconds

    # Compare the total seconds
    return total_seconds1 < total_seconds2

# Part 3

def songs_shorter_than(songs: list[Song], max_duration: Duration) -> list[Song]:
    # Filter songs with duration shorter than max_duration
    return [song for song in songs if shorter_duration_than(song.duration, max_duration)]


# Part 4

def running_time(songs: list[Song], playlist: list[int]) -> Duration:
    # Initialize total seconds
    total_seconds = 0

    for index in playlist:
        # Check if the index is within the valid range
        if 0 <= index < len(songs):
            song_duration = songs[index].duration
            # Convert each duration to seconds and add to the total
            total_seconds += song_duration.minutes * 60 + song_duration.seconds

    # Convert total seconds back to minutes and seconds
    total_minutes = total_seconds // 60
    remaining_seconds = total_seconds % 60

    # Return the total running time as a Duration object
    return Duration(total_minutes, remaining_seconds)

# Part 5

def validate_route(city_links: list[list[str]], route: list[str]) -> bool:
    # An empty or single-city route is always valid
    if len(route) <= 1:
        return True

    # Iterate through consecutive city pairs in the route
    for i in range(len(route) - 1):
        city1, city2 = route[i], route[i + 1]
        # Check if the pair exists in city_links in either order
        if [city1, city2] not in city_links and [city2, city1] not in city_links:
            return False  # If a pair is not linked, the route is invalid

    # All consecutive pairs have links, so the route is valid
    return True


# Part 6

from typing import Optional


def longest_repetition(numbers: list[int]) -> Optional[int]:
    if not numbers:
        return None

    max_length = 0
    max_start_index = 0
    current_length = 1
    current_start_index = 0

    # Iterate through the list to find contiguous sequences
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:  # Current sequence continues
            current_length += 1
        else:  # Current sequence ends
            # Update max sequence if current is longer
            if current_length > max_length:
                max_length = current_length
                max_start_index = current_start_index
            # Reset current sequence
            current_length = 1
            current_start_index = i

    # Final check in case the longest sequence ends at the last element
    if current_length > max_length:
        max_start_index = current_start_index

    return max_start_index
