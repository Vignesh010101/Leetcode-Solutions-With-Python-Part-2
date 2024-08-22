class Solution:
  def maximizeTheProfit(self, n: int, arr: List[List[int]]) -> int:
    res, pos = [0] * (n + 1), 0
    arr.sort(key=lambda x: (x[1], x[0]))

    for i in range(1, n + 1):
      best_val = res[i - 1]
      while pos < len(arr) and arr[pos][1] == i - 1:
        best_val = max(best_val, arr[pos][2] + res[arr[pos][0]])
        pos += 1
      res[i] = best_val
    
    return res[-1]