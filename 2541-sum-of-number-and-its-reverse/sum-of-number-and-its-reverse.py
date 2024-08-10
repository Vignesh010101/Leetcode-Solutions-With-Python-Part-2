class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        digits = []
        while num > 0:
            digits.append(num % 10)
            num = num // 10

        digits.reverse()
        hi, lo = 0, len(digits) - 1
        while hi <= lo:
            if hi == lo:
                if digits[hi] % 2 == 0:
                    break
                else:
                    return False
            if digits[hi] == digits[lo]:
                hi += 1
                lo -= 1
            elif digits[hi] == 1 and digits[hi] != digits[lo]:
                digits[hi] -= 1
                digits[hi+1] += 10
                hi += 1
                if lo != hi:
                    digits[lo] += 10
                    digits[lo-1] -= 1
                    cur = lo - 1
                    while digits[cur] < 0:
                        digits[cur] = 0
                        digits[cur-1] -= 1
                        cur -= 1
                
            elif digits[hi]-1 == digits[lo] and hi + 1 < lo:
                    digits[hi]-= 1
                    digits[hi+1] += 10
                    hi += 1
                    lo -= 1
                # else:
                #     return False
            elif digits[hi] - 1 == digits[lo] + 10 and hi + 1 < lo:
                digits[hi] -= 1
                digits[hi+1] += 10
                digits[lo-1] -= 1
                cur = lo - 1
                while digits[cur] < 0:
                    digits[cur] = 0
                    digits[cur-1] -= 1
                    cur -= 1     
                digits[lo] += 10
            elif hi-1>=0 and lo+1<=len(digits)-1 and digits[hi-1] == 1 and digits[lo+1] == 1:
                digits[hi-1] -= 1
                digits[hi] += 10
                digits[lo+1] += 10
                digits[lo] -= 1
                cur = lo
                while digits[cur] < 0:
                    digits[cur] = 0
                    digits[cur-1] -= 1
                    cur -= 1
                lo += 1
            else:
                return False
        return True