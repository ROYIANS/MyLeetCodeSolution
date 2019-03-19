import copy

class Solution:
    def subarraySum(self, nums, k):
        count = 0
        sums = 0
        while len(nums) > 1:
            tmp = copy.deepcopy(nums)
            while len(tmp) > 0:
                sums = sums + tmp[-1]
                if sums == k:
                    count = count + 1
                    if len(tmp) > 1:
                        if tmp[-2] != 0:
                            nums.pop()
                            sums = 0
                            break
                    elif len(tmp) == 1:
                        nums.pop()
                        sums = 0
                        break
                    tmp.pop()
                else:
                    tmp.pop()
                if len(tmp) == 0:
                    sums = 0
                    nums.pop()
        if nums[0] == k or nums[0] == 0:
            count = count + 1
        return count


if __name__ == "__main__":
    s = Solution()
    a = [-1,1,-1]
    t = -1
    print(s.subarraySum(a,t))