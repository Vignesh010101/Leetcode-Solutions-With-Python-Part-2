class Solution:
	def minimumCost(self, s: str) -> int:

		result = 0

		length = len(s)

		for index in range(1 ,  length):

			if s[index - 1] == s[index]:

				result = result + 0

			else:

				result = result + min(index , length - index)

		return result