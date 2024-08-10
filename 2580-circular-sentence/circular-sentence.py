class Solution:
	def isCircularSentence(self, sentence: str) -> bool:

		sentence = sentence.split()
		first_word = sentence[0]
		last_word = sentence[-1]

		if first_word[0] != last_word[-1]:
			return False

		for i in range(len(sentence)-1):

			first_word = sentence[i]
			last_word = sentence[i+1]

			if first_word[-1] != last_word[0]:
				return False

		return True
		