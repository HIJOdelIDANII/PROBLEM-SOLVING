class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            med = (l + r) // 2
            if nums[med] == target:
                return med
            elif nums[med] > target:
                r = med - 1
            else:
                l = med + 1
        return -1

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            med = (l + r) // 2
            if self.search(matrix[med], target) != -1:
                return True
            elif matrix[med][0] > target:
                r = med - 1
            elif matrix[med][-1] < target:
                l = med + 1
            else:
                return False
        return False
