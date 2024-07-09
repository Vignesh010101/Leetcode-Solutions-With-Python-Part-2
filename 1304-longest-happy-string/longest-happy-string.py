class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Initialize a dictionary to store character counts
        char_count = {"a": a, "b": b, "c": c}
        # Initialize an empty string to store the constructed happy string
        result = ""

        # Greedily construct the happy string
        while char_count:
            # Sort characters based on counts in descending order
            sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
            max_char, max_count = sorted_chars[0]

            # Check if it's possible to put max_char into result without violating consecutive character constraint
            if len(result) >= 2 and result[-1] == result[-2] == max_char:
                # If not, check if there's another character available to put
                if len(sorted_chars) > 1 and sorted_chars[1][1] > 0:
                    max_char = sorted_chars[1][0]
                else:
                    break

            # If max_count is less than or equal to 0, break the loop
            if max_count <= 0:
                break

            # Append max_char to result and decrement its count in char_count
            result += max_char
            char_count[max_char] -= 1

        # Return the constructed happy string
        return result