class Solution:
  def lenLongestFibSubseq(self, arr: list[int]) -> int:
    longest_subsequence = 0
    index_from_value_table = {x: i for i, x in enumerate(arr)}
    subsequence_length_dict = defaultdict(lambda: 2)
    for k, k_val in enumerate(arr):
      jlo = bisect_right(arr, k_val // 2, hi=k)
      for j_val in arr[jlo:k]:
        j = index_from_value_table[j_val]
        i = index_from_value_table.get(k_val - j_val, None)
        if i is None: continue
        seq = subsequence_length_dict[i, j] + 1
        subsequence_length_dict[j, k] = seq
        longest_subsequence = max(longest_subsequence, seq)
    return longest_subsequence