class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        our_set = set()
        for i in nums:
            if i in our_set:
                return True
            else:
                our_set.add(i)
        return False
    