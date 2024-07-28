class Solution:
    def minSwaps(self, s: str) -> int:
        stack=[]
        swaps=0
        for c in s:
            if c=='[':
                stack.append(c)
            else:
                if stack and stack[-1]=='[':
                    stack.pop()
                else:
                    swaps+=1
        return (swaps+1)//2