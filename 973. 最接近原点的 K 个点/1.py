import math


class Solution:

    @staticmethod
    def distance(item):
        return math.sqrt(pow(abs(item[0]),2) + pow(abs(item[1]), 2))

    def kClosest(self, points, K):
        re = []
        items = list(enumerate(points))
        # print(sorted(items,key=(lambda x:x[1][1])))
        for item in items:
            dis = self.distance(item[1])
            re.append([item, dis])
        result = sorted(re,key=(lambda x:x[1]))
        fn = []
        for i in range(K):
            fn.append(result[i][0][1])
        return fn


if __name__ == "__main__":
    s = Solution()
    pointss = [[3, 3], [5, -1], [-2, 4]]
    KK = 2
    print(s.kClosest(pointss,KK))


# 或者
#    def kClosest(self, points, K):
#        return sorted(points,key=(lambda x: (math.sqrt(pow(abs(x[0]), 2) + pow(abs(x[1]), 2)))))[:K]