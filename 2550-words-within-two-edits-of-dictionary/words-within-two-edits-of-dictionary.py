class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def isWithinEditDistance(word1, word2):
            count = 0
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    count += 1
                    if count > 2:
                        return False
            
            return True
        
        matching_queries = []
        for query in queries:
            for word in dictionary:
                if isWithinEditDistance(query, word):
                    matching_queries.append(query)
                    break
        return matching_queries    