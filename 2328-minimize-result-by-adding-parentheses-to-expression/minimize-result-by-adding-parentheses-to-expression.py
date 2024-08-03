class Solution:
    def minimizeResult(self, expression: str) -> str:
        mid = expression.index('+')
        length = len(expression)
        
        # calculate combinations for first and second number - O(n)
        num1_pairs = [(expression[:i], expression[i:mid]) for i in range(mid)]
        num2_pairs = [(expression[mid + 1:i], expression[i:]) for i in range(length, mid + 1, -1)]
    
    
        # define a variable to track the minimum and its associated indices for combinations
        minimum = (float('inf'), 0, length - 1)

        # go through all combinations - O(n ** 2)
        for i, num1_pair in enumerate(num1_pairs):
            for j, num2_pair in enumerate(num2_pairs):
                res = (1 if i == 0 else int(num1_pair[0])) * (int(num1_pair[1]) + int(num2_pair[0])) * (
                    1 if j == 0 else int(num2_pair[1]))
                if res < minimum[0]:
                    minimum = (res, i, j)
        
        # retrieve the indices for combinations with minimum result
        i = minimum[1]
        j = minimum[2]
        return num1_pairs[i][0] + '(' + num1_pairs[i][1] + '+' + num2_pairs[j][0] + ')' + num2_pairs[j][1]