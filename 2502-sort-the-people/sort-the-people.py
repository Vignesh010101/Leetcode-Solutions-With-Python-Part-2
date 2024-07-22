class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [vy for _,vy in sorted(zip(heights,names), reverse=True)]