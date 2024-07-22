class Solution:
    def maximumBinaryString(self, binary: str) -> str:

        if not '0' in binary: return binary
        left0, zeros = binary.find('0'), binary.count('0')
        
        ans = '1'*(left0+zeros-1) + '0'
        return ans.ljust(len(binary), '1')