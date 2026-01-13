class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_day = {}  # task_type -> last day it was performed
        day = 0
        
        for task in tasks:
            day += 1
            if task in last_day:
                # Need to wait at least space days
                day = max(day, last_day[task] + space + 1)
            last_day[task] = day
        
        return day