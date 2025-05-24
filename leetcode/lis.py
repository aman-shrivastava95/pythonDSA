from typing import List
from bisect import bisect_left

class Solution:

    def LisBinarySearch(self, nums: List[int]) -> int:
        arr = []
        for x in nums:
            idx = bisect_left(arr, x)
            if idx == len(arr):
                arr.append(x)
            else:
                arr[idx] = x
        # please note that the arr may not contain the actual lis, it will alawys have the length of the list
        return len(arr)


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
