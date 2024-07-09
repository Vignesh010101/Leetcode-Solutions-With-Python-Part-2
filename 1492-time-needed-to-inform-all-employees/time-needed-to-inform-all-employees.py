from collections import defaultdict
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        master_maps = defaultdict(list) # boss: employees
        for i, m in enumerate(manager):
            if m!= -1:
                master_maps[m].append(i)
        def get_time_inform(leader):
            if leader not in master_maps:
                return 0
            max_time = 0
            for sub_leader in master_maps[leader]:
                max_time = max(max_time, informTime[leader] + get_time_inform(sub_leader))
            return max_time
        
        return get_time_inform(headID)
