from data import*
from hw2 import*

import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1

    def test_create_rectangle_standard(self):
    #test two distinct points to form a standard rectangle
        point_a = Point(2,2)
        point_b = Point(10,10)
        self.assertEqual(create_rectangle(point_a,point_b), Rectangle(Point(2,10), Point(10,2)))
    def test_create_rectangle_line(self):
    #test two distinct points to form line
        point_a = Point(0,0)
        point_b = Point(0,10)
        self.assertEqual(create_rectangle(point_a, point_b), Rectangle(Point(0,10), Point(0,0)))
    def test_create_rectangle_negative(self):
    #test two distinct negative points to form standard rectangle
        point_a = Point(-2,4)
        point_b = Point(4,-2)
        self.assertEqual(create_rectangle(point_a, point_b), Rectangle(Point(-2,4), Point(4,-2)))

    # Part 2

    def test_shorter_duration_than_true(self):
        duration1 = Duration(1, 10)  # 1 hour 20 minutes
        duration2 = Duration(1, 30)  # 1 hour 30 minutes
        self.assertTrue(shorter_duration_than(duration1, duration2), True)

    def test_shorter_duration_than_false(self):
        duration1 = Duration(4,0)  # 2 hours
        duration2 = Duration(3,1)  # 1 hour 30 minutes
        self.assertFalse(shorter_duration_than(duration1, duration2), False)

    def test_shorter_duration_than_equal(self):
        duration1 = Duration(1, 30)  # 1 hour 30 minutes
        duration2 = Duration(1, 30)  # 1 hour 30 minutes
        self.assertFalse(shorter_duration_than(duration1, duration2), False) # Equal durations should return False

    # Part 3
    def test_songs_shorter_than_some(self):
        # Test case where some songs are shorter than max_duration
        songs = [
            Song("Artist A", "Song A", Duration(3, 0)),
            Song("Artist B", "Song B", Duration(4, 0)),
            Song("Artist C", "Song C", Duration(3, 15))
        ]
        max_duration = Duration(3, 30)
        result = songs_shorter_than(songs, max_duration)
        expected = [songs[0], songs[2]]  # Songs A and C are shorter than 3:30
        self.assertEqual(result, expected)

    def test_songs_shorter_than_all(self):
        # Test case where all songs are shorter than max_duration
        songs = [
            Song("Artist D", "Song D", Duration(2, 45)),
            Song("Artist E", "Song E", Duration(3, 10))
        ]
        max_duration = Duration(4, 0)
        result = songs_shorter_than(songs, max_duration)
        expected = songs  # All songs are shorter than 4:00
        self.assertEqual(result, expected)

    def test_songs_shorter_than_none(self):
        # Test case where no songs are shorter than max_duration
        songs = [
            Song("Artist F", "Song F", Duration(5, 0)),
            Song("Artist G", "Song G", Duration(6, 0))
        ]
        max_duration = Duration(4, 0)
        result = songs_shorter_than(songs, max_duration)
        expected = []  # No songs are shorter than 4:00
        self.assertEqual(result, expected)

    # Part 4

    def test_running_time_standard_playlist(self):
        songs = [
            Song("Decemberists", "June Hymn", Duration(4, 30)),
            Song("Broken Bells", "October", Duration(3, 40)),
            Song("Kansas", "Dust in the Wind", Duration(3, 29)),
            Song("Local Natives", "Airplanes", Duration(3, 58))
        ]
        playlist = [0, 2, 1, 3, 0]
        result = running_time(songs, playlist)
        expected = Duration(20, 7)  # Total time is 20 minutes and 7 seconds
        self.assertEqual(result, expected)

    def test_running_time_with_out_of_range_indices(self):
        songs = [
            Song("Decemberists", "June Hymn", Duration(4, 30)),
            Song("Broken Bells", "October", Duration(3, 40)),
        ]
        playlist = [0, 1, 2, -1, 0]  # Indices 2 and -1 are out of range
        result = running_time(songs, playlist)
        expected = Duration(12, 40)  # Only valid indices contribute (4:30 + 3:40 + 4:30)
        self.assertEqual(result, expected)

    def test_running_time_empty_playlist(self):
        songs = [
            Song("Artist A", "Song A", Duration(2, 30)),
            Song("Artist B", "Song B", Duration(3, 15)),
        ]
        playlist = []  # No songs in the playlist
        result = running_time(songs, playlist)
        expected = Duration(0, 0)  # Total time is 0 minutes and 0 seconds
        self.assertEqual(result, expected)

    # Part 5

    def test_validate_route_valid(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = ['san luis obispo', 'santa margarita', 'atascadero']
        self.assertTrue(validate_route(city_links, route))

    def test_validate_route_invalid(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = ['san luis obispo', 'atascadero']
        self.assertFalse(validate_route(city_links, route))

    def test_validate_route_single_city(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = ['san luis obispo']
        self.assertTrue(validate_route(city_links, route))

    def test_validate_route_empty(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = []
        self.assertTrue(validate_route(city_links, route))

    # Part 6

    def test_longest_repetition_standard(self):
        numbers = [1, 1, 2, 2, 1, 1, 1, 3]
        result = longest_repetition(numbers)
        self.assertEqual(result, 4)  # Longest sequence of 1s starts at index 4

    def test_longest_repetition_multiple_same_length(self):
        numbers = [4, 4, 5, 5, 4, 4]
        result = longest_repetition(numbers)
        self.assertEqual(result, 0)  # First longest sequence of 4s starts at index 0

    def test_longest_repetition_single_element(self):
        numbers = [7]
        result = longest_repetition(numbers)
        self.assertEqual(result, 0)  # Only one element, starting at index 0

    def test_longest_repetition_empty_list(self):
        numbers = []
        result = longest_repetition(numbers)
        self.assertIsNone(result)  # Empty list, so result is None

    def test_longest_repetition_entire_list_same(self):
        numbers = [9, 9, 9, 9]
        result = longest_repetition(numbers)
        self.assertEqual(result, 0)  # Entire list is the longest sequence starting at index 0





if __name__ == '__main__':
    unittest.main()
