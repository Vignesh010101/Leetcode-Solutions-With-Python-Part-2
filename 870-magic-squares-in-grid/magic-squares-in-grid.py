class Solution:
	def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

		result = 0
		rows = len(grid)
		cols = len(grid[0])

		for row in range(rows - 2):
			for col in range(cols - 2):

				count = 0

				for num in range(1, 10):

					if num in grid[row][col : col + 3] + grid[row + 1][col : col + 3] + grid[row + 2][col : col + 3]:
						count = count + 1
					else:
						break

				row1 = sum(grid[row][col : col + 3])
				row2 = sum(grid[row + 1][col : col + 3])
				row3 = sum(grid[row + 2][col : col + 3])

				diagonal1 = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
				diagonal2 = grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col]

				col1 = grid[row][col] + grid[row + 1][col] + grid[row + 2][col]
				col2 = grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1]
				col3 = grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2]

				if count == 9 and row1 == 15 and row2 == 15 and row3 == 15 and diagonal1 == 15 and diagonal2 == 15 and col1 == 15 and col2 == 15 and col3 == 15:
				
					result = result + 1

		return result