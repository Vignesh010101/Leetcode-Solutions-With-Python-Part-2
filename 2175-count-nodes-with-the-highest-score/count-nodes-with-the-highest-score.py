class Solution:
    def dfs(self, root, tree, cnt):
        if not tree[root]:
            cnt[root] = len(tree)-1
            return 1
        score, sum_children_nodes = 1, 0
        for child in tree[root]:
            cnt_children_nodes = self.dfs(child, tree, cnt)
            score *= cnt_children_nodes
            sum_children_nodes += cnt_children_nodes
        cnt[root] = score * (len(tree) - sum_children_nodes - 1 if root else 1)
        return sum_children_nodes + 1
      

    def countHighestScoreNodes(self, parents: List[int]) -> int:
        tree = [[] for _ in range(len(parents))]
        cnt = [0]*len(parents)
        for child, parent in enumerate(islice(parents, 1, None), start = 1):
            tree[parent].append(child)
        self.dfs(0, tree, cnt)
        return cnt.count(max(cnt))

        
        