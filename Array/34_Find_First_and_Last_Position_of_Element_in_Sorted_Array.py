class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums: List[int], target: int):
            left, right = 0, len(nums) - 1
            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] > target:
                    right = middle - 1
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    return middle
            return -1

        index = binarySearch(nums, target)
        if index == -1: 
            return [-1, -1]
        
        left, right = index, index
        while left - 1 >= 0 and nums[left-1] == target:
            left -= 1
        while right + 1 < len(nums) and nums[right+1] == target:
            right += 1

        return [left, right] 

