class Solution:
    def largestPalindromic(self, num: str) -> str:
        freq = Counter(num)
        mid = next((ch for ch in "9876543210" if freq[ch]&1), '')
        half = ''.join(ch*(freq[ch]//2) for ch in "0123456789")
        return (half[::-1] + mid + half).strip('0') or '0'