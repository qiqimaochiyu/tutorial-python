# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        L = []
        for i in sorted(intervals, key=lambda x:x.start):
            if L and i.start <= L[-1].end:
                L[-1].end = max(L[-1].end, i.end)
            else:
                L.append(i)
        return L
