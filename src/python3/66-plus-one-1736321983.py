class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            i = len(digits) - 1
            while i >= 0:
                if digits[i] == 9:
                    digits[i] = 0
                    i -= 1
                else:
                    break
            if i < 0:
                digits = [1] + digits
            else:
                digits[i] += 1
            return digits