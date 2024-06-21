# To effectively check prime, we need a prime tester => Sieve of Eratosthenes (Google it if don't know)
# We put this here because Leetcode only do this part once for all solutions so we can reuse and save some time
def getAllPrimes():
    n = 10 ** 5
    prime = [True for _ in range(n + 1)]
    prime[0] = prime[1] = False
    x, y = 2, int(sqrt(n)) + 1
    while x < y:
        if prime[x]: 
            for i in range(x * 2, n + 1, x):
                prime[i] = False
        x += 1
    return prime    
primes = getAllPrimes()     # primes[number] = True if prime, False otherwise

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        # all possible PATH = [node's one chain] + node peak + [node's another chain] 
        # for each node we need three informations:
        # 1. for each child node: number of chains contains 0 prime
        # 2. for each child node: number of chains contains 1 prime
        # 3. number of valid PATH with peak at node => sum for all nodes will give us result
        # get all neighbors
        neighbors = [[] for _ in range(n + 1)]
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        # define dfs that will help us collect the three informations & update result
        result = [0]
        visited = dict()
        def dfs(node, prev):
            visited[node] = 0
            # Step1: get info from child nodes
            allChain0s, allChain1s = [], []
            total0, total1 = 0, 0
            for child in neighbors[node]:
                # since we have a undirected tree, to avoid inf-loop, we need to ignore visited states
                if child == prev: continue
                chain0, chain1 = dfs(child, node)
                total0 += chain0
                total1 += chain1
                allChain0s.append(chain0) 
                allChain1s.append(chain1)
            # Step2: combine to create new info for the current node
            # current node is prime
            if primes[node]: 
                # 1. all chains ending at node will have >0 prime
                currChain0 = 0  
                # 2. 1 (itself) + all previous 0-chains ending at node will have 1 prime
                currChain1 = 1 + total0
                # 3. node as peak combine with any 0 chains is valid
                combTotal = 0
                for tmp0 in allChain0s:  # count combinations of two 0 chains from different childs
                    combTotal += (tmp0 * (total0 - tmp0))
                result[0] += (total0 + combTotal // 2)
            # current node is not prime
            else:
                # 1. chains ending at node will have 0 prime IFF the original chain contain 0 prime
                currChain0 = 1 + total0
                # 2. chains ending at node will have 1 prime IFF the original chain contain 1 prime
                currChain1 = total1
                # 3. node as peak combine with single 1 chain OR 1x1chain + 1x0chain at different childs is valid
                combTotal = 0
                for i in range(len(allChain0s)):  # count combinations of 1x1chain + 1x0chain from different childs
                    tmp0, tmp1 = allChain0s[i], allChain1s[i]
                    combTotal += (tmp0 * (total1 - tmp1)) + (tmp1 * (total0 - tmp0))
                result[0] += (total1 + combTotal // 2)
            return currChain0, currChain1
        dfs(1, inf)
        return result[0]


        