class Solution:

  def is_same_frequency(self, freq, k: int):
    return all([freq[i] == k or freq[i] == 0 for i in freq])

  def count_substrings(self, s: str, k: int) -> int:
    count, distinct = 0, len(set([i for i in s]))

    for l in range(1, distinct + 1):
      max_l, freq = l * k, defaultdict(int)
      pos_s, pos_e = 0, max_l - 1

      for i in range(pos_s, min(pos_e + 1, len(s))):
        freq[s[i]] += 1

      while pos_e < len(s):
        if self.is_same_frequency(freq, k):
          count += 1

        freq[s[pos_s]] -= 1
        pos_s, pos_e = pos_s + 1, pos_e + 1
        if pos_e < len(s):
          freq[s[pos_e]] += 1
    return count

  def countCompleteSubstrings(self, word: str, k: int) -> int:
    groups = [[]]
    for c in word:
      if len(groups[-1]) == 0:
        groups[-1].append(c)
      elif abs(ord(groups[-1][-1]) - ord(c)) <= 2:
        groups[-1].append(c)
      else:
        groups.append([c])

    res = 0
    for g in groups:
      res += self.count_substrings(''.join(g), k)

    return res