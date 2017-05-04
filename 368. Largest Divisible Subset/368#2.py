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

        S = []
        for i in range(n):
            sub = []
            for j in range(len(S)):
                if nums[i] % nums[j] == 0:
                    sub.append(S[j])
            if len(sub):
                S.append(max(sub, key=len) | {nums[i]})
            else:
                S.append({nums[i]})

        return list(max(S, key=len))

s = Solution()
print s.largestDivisibleSubset([3,2,4,8])