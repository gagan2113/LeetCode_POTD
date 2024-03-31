class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt, res, l, m = [0] * (len(nums) + 1), 0, 0, 0
        for n in nums:
            cnt[n] += 1
            if cnt[n] == 1:
                k -= 1
                if (k < 0):
                    cnt[nums[m]] = 0
                    m += 1
                    l = m
            if k <= 0:
                while(cnt[nums[m]] > 1):
                    cnt[nums[m]] -= 1
                    m += 1
                res += m - l + 1
        return res  