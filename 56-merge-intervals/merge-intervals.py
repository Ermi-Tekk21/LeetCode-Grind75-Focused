class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        newIntervals = [intervals[0]]  

        def merge(f1, f2):
            if f1[1] >= f2[0]: 
                return [min(f1[0], f2[0]), max(f1[1], f2[1])]
            else:
                return None 

        size = len(intervals)

        for i in range(1, size):
            merged = merge(newIntervals[-1], intervals[i])
            if merged: 
                newIntervals[-1] = merged
            else:  
                newIntervals.append(intervals[i])

        return (newIntervals)