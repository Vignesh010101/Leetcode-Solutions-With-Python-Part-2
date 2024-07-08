from itertools import zip_longest
from typing import Iterable


class Solution:
    def printVertically(self, s: str) -> Iterable[str]:
        return map(str.rstrip, map(''.join, zip_longest(*s.split(), fillvalue=' ')))