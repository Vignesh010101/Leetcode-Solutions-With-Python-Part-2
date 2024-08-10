from collections import defaultdict

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
      videos = defaultdict(lambda: [(0, ''), 0])

      for c, i, v in zip(creators, ids, views):
        videos[c][1] += v
        vv, vid = videos[c][0]
        if v > vv or (v == vv and (i < vid or vid == '')): videos[c][0] = (v, i)
      
      most_views = max([v for _, v in videos.values()])
      return [[c, vid] for c, ((vv, vid), v) in videos.items() if v == most_views]