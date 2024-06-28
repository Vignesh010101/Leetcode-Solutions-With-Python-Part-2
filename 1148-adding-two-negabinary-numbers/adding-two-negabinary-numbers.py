class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_len = len(arr1)
        arr2_len = len(arr2)
        longest_len = max([arr1_len, arr2_len])
        # Allocate memory space for answer
        answer_len = arr1_len + arr2_len + 3
        answer = [0] * answer_len

        for i in range(longest_len):
            index = -1 * (i+1)
            value = answer[index]
            # Sum the column
            if (i<arr1_len) and arr1[index]:
                value += 1
            if (i<arr2_len) and arr2[index]:
                value += 1
            if value in [0,1]:
                answer[index] = value
            elif value >= 2:
                # Add to the next columns
                if answer[index-1] > 0:
                    answer[index-1] -= 1
                    answer[index] = value - 2
                else:
                    answer[index-1] = 1
                    answer[index-2] = 1
                    answer[index] = value - 2
        if 1 not in answer:
            answer = [0]
        else:
            answer = answer[answer.index(1):]
        return answer