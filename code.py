import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int):
        return bisect.bisect_left(nums, target)
