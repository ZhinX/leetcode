class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)
        d = []
        for k in range(n):
            d.append([-1] * n)

        for i in range(n):
            d[i][i] = nums[i]

        if n % 2 != 0:
            i = 0
            j = 2

        else:
            for i in range(n-1):
                d[i][i+1] = max(d[i][i], d[i+1][i+1])
            i = 0
            j = 3

        while j <= n-1:
            d[i][j] = max(min(d[i+2][j], d[i+1][j-1]) + nums[i], min(d[i][j-2], d[i+1][j-1]) + nums[j])
            if j == n - 1:
                j = n + 1 - i
                i = 0
            else:
                i += 1
                j += 1

        result = d[0][n-1]
        return True if float(result) >= float(sum(nums)) / 2 else False


s = Solution()
print s.PredictTheWinner([1, 3, 1])
