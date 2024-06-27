class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
		# Build the frequency dictionary
        freq_map = collections.defaultdict(int)
        maxFreq = 0
        for code in barcodes:
            freq_map[code] += 1
            if freq_map[code] > freq_map[maxFreq]:
                maxFreq = code
        
        n = len(barcodes)
        idx = 0
        res = [0]*n
        
		# Fill in the result array with the code with maximum frequency
        idx = 0
        for v in range(freq_map[maxFreq]):
            res[idx] = maxFreq
            idx += 2
        
        del freq_map[maxFreq]
        
		# Fill the rest of the codes in the result array
        for k,v in freq_map.items():
            for _ in range(v):
                if idx >= n:
                    idx = 1
                res[idx] = k
                idx += 2
                
        return res