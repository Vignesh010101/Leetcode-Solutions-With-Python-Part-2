class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        graph = {}

        def find(char):
            if graph[char] == char:
                return char
            else:
                return find(graph[char])

        stack = [e for e in equations if e[1] == "="]
        inequs = [e for e in equations if e[1] == "!"]

        for char in "".join(equations):
            graph[char] = char

        while len(stack) > 0:
            e = stack.pop()
            graph[find(e[0])] = find(e[3])
        
        for ine in inequs:
            x = ine[0]; y = ine[3]
            if find(x) == find(y):
                return False
        return True