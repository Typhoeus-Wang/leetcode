class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1 or num == 0:
            return True
        
        left, right = 1, num
        while left <= right:
            middle = left + (right - left) // 2
            
            middle_square = middle * middle
            if middle_square > num:
                right = middle - 1
            elif middle_square < num:
                left = middle + 1
            else:
                return True
        
        return False

