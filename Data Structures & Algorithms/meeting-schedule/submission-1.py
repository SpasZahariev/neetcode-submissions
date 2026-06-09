"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # todo input validation
        if not intervals:
            return True
            
        # sort the intervals nlogn
        intervals.sort(key=lambda x: x.start)

        # iterate iand check if there is any overlap
        prev = intervals[0]
        for i in range(1, len(intervals)):
            item = intervals[i]

            # check
            if prev.start <= item.start < prev.end:
                return False
            prev = item
        
        return True