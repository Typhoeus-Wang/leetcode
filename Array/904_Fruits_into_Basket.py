import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        left, right = 0, 0
        max_so_far = 0

        while right < len(fruits):

            count[fruits[right]] = count.get(fruits[right], 0) + 1

            # reduce the sliding window size
            while len(count) > 2:
                count[fruits[left]] -= 1
                if not count[fruits[left]]:
                    count.pop(fruits[left])
                left += 1
            max_so_far = max(max_so_far, right - left + 1)
            right += 1
        return max_so_far