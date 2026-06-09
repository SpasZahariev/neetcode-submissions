"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # todo input validation
        if not intervals:
            return 0
        
        # sort
        intervals.sort(key=lambda item: item.start)

        # keep a dynamic array of rooms. If there is an overlap increment the list with an item. To show that a room is taken
        rooms = [intervals[0]]

        # worst case would be if every meeting is colliding with every other meeting. We would need to do n^2 checks

        for i in range(1, len(intervals)):
            item = intervals[i]

            # try seeing if room is free
            found_room = False
            for room in rooms:
                if room.end <= item.start:
                    found_room = True
                    room.start = item.start
                    room.end = item.end
                    break
            if not found_room:
                rooms.append(item)
        
        return len(rooms)