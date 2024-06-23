class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        block_size = int(n ** 0.5) + 1
        blocks = [0] * block_size

        # Preprocess queries to keep the original index
        queries = [sorted(query) + [index] for index, query in enumerate(queries)]

        # Process heights and update blocks
        for index, height in enumerate(heights):
            blocks[index // block_size] = max(height, blocks[index // block_size])

        # Sort queries based on block index
        queries.sort(key=lambda x: x[0] // block_size)

        result = [-1] * len(queries)

        # Iterate through the sorted queries
        for query in queries:
            left, right, index = query

            # Directly set the result if right building is greater than left building
            if heights[right] > heights[left]:
                result[index] = right
                continue

            # Set the result if the left and right indices are the same
            elif right == left:
                result[index] = right
                continue

            right_block = right // block_size
            right_block_val = blocks[right_block]
            flag = True

            # Check if the right block is higher than both left and right buildings
            if right_block_val > heights[left] and right_block_val > heights[right]:
                # Iterate through the buildings in the block to find the leftmost building
                for i, value in enumerate(heights[right_block * block_size : block_size * (right_block + 1) + 1]):
                    if value > heights[left] and value > heights[right] and right_block * block_size + i > right:
                        result[index] = right_block * block_size + i
                        flag = False
                        break
                else:
                    right_block += 1

            else:
                right_block += 1
                flag = True

            # Continue iterating to find the leftmost building
            if flag:
                while right_block < len(blocks) and (blocks[right_block] < heights[left] or blocks[right_block] < heights[right]):
                    right_block += 1
                if right_block >= len(blocks):
                    continue

                # Iterate through the buildings in the block to find the leftmost building
                for i, value in enumerate(heights[right_block * block_size : block_size * (right_block + 1) + 1]):
                    if value > heights[left] and value > heights[right]:
                        result[index] = right_block * block_size + i
                        break

        return result