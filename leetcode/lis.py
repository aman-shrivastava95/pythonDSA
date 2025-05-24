from typing import List

class Solution:

    def LisBinarySearch(self, nums: List[int]) -> int:
        #TODO complete this method
        pass


    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1 for _ in range(len(nums))]
        # lis is length of lis ending at i
        res = 1
        for i in range(1, len(nums)):
            j = i - 1
            while j >= 0:
                if nums[i] > nums[j]:
                    lis[i] = max(lis[j] + 1 , lis[i])
                j-=1
            res = max(res, lis[i])
        return res