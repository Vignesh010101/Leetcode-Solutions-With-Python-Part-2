from collections import Counter

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        
        seen = set([id])
        queue = [id] 
        for i in range(level):

            temp = []
            while queue:
                
                curr = queue.pop(0)
                
                for val in friends[curr]:
                    if val not in seen:
                        seen.add(val)
                        temp.append(val)
         
            
            queue = temp[:]

        ans = []
        for val in queue:
            ans.extend(watchedVideos[val])

        ans = Counter(ans)

        return [item[0] for item in sorted(ans.items(), key= lambda x: (x[1], x[0]))]