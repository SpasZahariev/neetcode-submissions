"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # todo input validation
        if not intervals:
            return 0
        
        # sort
        intervals.sort(key=lambda item: item.start)

        # if the soonest ending room doesn't work, WE MUST allocate a new room
        # rooms heap
        rooms_heap = [intervals[0].end]

        # worst case would be if every meeting is colliding with every other meeting. We would need to do n^2 checks

        for i in range(1, len(intervals)):
            item = intervals[i]

            # if the earliest ending room is free -> we can reuse it!
            if rooms_heap[0] <= item.start:
                heapq.heappop(rooms_heap) # empty the old meeting room

            # allocate the room the the new meeting's end time
            heapq.heappush(rooms_heap, item.end)
        
        return len(rooms_heap)