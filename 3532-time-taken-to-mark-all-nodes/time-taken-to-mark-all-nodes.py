class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        # build graph
        graph = {}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
            if edge[1] not in graph:
                graph[edge[1]] = []
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        root = 0
        
        # calulating time needed to traverse the remaining graph for each node
        subRouteTimes = [0 for i in range(len(edges)+1)]
        visited = [False for i in range(len(edges)+1)]
        def dfs(node):
            maxTimes = 0
            visited[node] = True
            for num in graph[node]:
                if visited[num] is False:
                    time = dfs(num)
                    if num % 2 == 1:
                        time += 1
                    else:
                        time += 2
                    if time > maxTimes:
                        maxTimes = time
            subRouteTimes[node] = maxTimes
            return maxTimes
        
        dfs(root)

        visited = [False for i in range(len(edges)+1)]
        times = [0 for i in range(len(edges)+1)]
        # calculate times start from each node
        def dfs2(node):
            # calculate the minimum time needed to traverse the graph
            visited[node] = True
            maxTimes = 0
            for num in graph[node]:
                time = subRouteTimes[num]
                if num % 2 == 0:
                    time += 2
                else:
                    time += 1
                maxTimes = max(maxTimes, time)
            times[node] = maxTimes

            # to get the updated subRouteTimes, we only need to update node
            # since the graph now denote time start from other nodes other than node itself
            # get the first and second longest time that points to node to increase the efficiency
            fMax, sMax = 0, 0
            for num in graph[node]:
                time = subRouteTimes[num] + 1 if num % 2 == 1 else subRouteTimes[num] + 2
                if time > fMax:
                    sMax = fMax
                    fMax = time
                elif time > sMax:
                    sMax = time

            for num in graph[node]:
                if visited[num]:
                    continue

                # if the new root itself is the one with the longest time, we used the second longest instead
                selfTime = subRouteTimes[num] + 1 if num % 2 == 1 else subRouteTimes[num] + 2
                otherMax = fMax if selfTime < fMax else sMax
                
                
                prev = subRouteTimes[node]
                # update the graph and do the calculation recursively
                subRouteTimes[node] = otherMax
                dfs2(num)
                # recover the information after traversing the node
                subRouteTimes[node] = prev
        
        dfs2(root)



        return times