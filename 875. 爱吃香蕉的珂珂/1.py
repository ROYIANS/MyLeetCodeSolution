import math

class Solution:
    def possible(self, num, piles, H):
        hour = 0
        for item in piles:
            hour += math.ceil(item/num)
        if hour <= H:
            return True
        else:
            return False

    def minEatingSpeed(self, piles, H):
        if len(piles) == 1 and piles[0] <= H:
            return 1
        maxNum = max(piles)
        minNum = 1
        while self.possible(minNum,piles,H) is not True:
            midNum = math.floor((maxNum + minNum)/2)
            if(maxNum - minNum == 1):
                break
            if self.possible(midNum,piles,H):
                maxNum = midNum
            else:
                minNum = midNum
        return maxNum


if __name__ == "__main__":
    piles = [8]
    H = 9
    mes = Solution()
    s = mes.minEatingSpeed(piles, H)
    print(s)