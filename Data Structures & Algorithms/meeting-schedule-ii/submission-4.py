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
        
        # sort the meetings by start time
        # start a meeting and put it in a heap (ordered by min end times)
        # if the meeting that is ending soonest (top of heap) can't accomodate for a meeting -> we need a new meeting room

        # todo imput validation
        if not intervals:
            return 0

        intervals.sort(key=lambda item: item.start)

        allocated_until = []
        for i in intervals:
            start, end = i.start, i.end

            # check if we can reuse a room
            if allocated_until and allocated_until[0] <= start:
                heapq.heappop(allocated_until)

            heapq.heappush(allocated_until, end)

        return len(allocated_until)