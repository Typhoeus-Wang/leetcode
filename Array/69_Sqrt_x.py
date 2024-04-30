class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        if x == 0:
            return 0
        
        left = 1
        right = x

        while left <= right:
            middle = left + (right - left) // 2

            square_mid = middle * middle

            if square_mid > x:
                right = middle - 1
            elif square_mid < x:
                left = middle + 1
            else:
                return middle
        
        return int(right)