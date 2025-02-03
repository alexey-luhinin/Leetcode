class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort()

        for i in range(1, len(intervals)):
            if intervals[i-1][1] > intervals[i][0]:
                return False
        
        return True

sol = Solution()
print(sol.canAttendMeetings([[0,30], [5,10], [15, 20]]))
print(sol.canAttendMeetings([[7,10], [2,4]]))
print(sol.canAttendMeetings([[7,10], [2,7]]))
