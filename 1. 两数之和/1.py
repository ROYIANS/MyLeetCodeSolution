#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution:
    def twoSum(self, nums, target):
        re = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    re.append(i)
                    re.append(j)
        return re


if __name__ == "__main__":
    s = Solution()
    nums = [1, 4, 2, 5, 9]
    target = 11
    print(s.twoSum(nums, target))
