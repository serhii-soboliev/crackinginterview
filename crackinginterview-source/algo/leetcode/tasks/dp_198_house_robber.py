class HouseRobber:

    def rob(self, nums) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        spoil = [0] * n
        spoil[0] = nums[0]
        spoil[1] = max(nums[0], nums[1])
        for i in range(2, n):
            spoil[i] = max(spoil[i-1], spoil[i-2]+nums[i])
        return max(spoil[n-1], spoil[n-2])



