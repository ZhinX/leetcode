class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not len(nums):
            return nums

        nums = sorted(nums)
        n = len(nums)
        dp = [0] * n
        parents = [0] * n

        dp[0] = 1
        parents[0] = -1
        for i in range(1, n):
            candidates = []
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    candidates.append(dp[j] + 1)
                else:
                    candidates.append(1)
            dp[i] = max(candidates)
            # if dp[i] is 1, then nums[i] must be a first candidate(can't be divided by any element ahead)
            parents[i] = candidates.index(dp[i]) if dp[i] != 1 else -1

        result = []
        index = dp.index(max(dp))
        while index != -1:
            result.insert(0, nums[index])
            index = parents[index]

        return result

s = Solution()
print s.largestDivisibleSubset([3,4,16,8])
