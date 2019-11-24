class MaxSubArray:

    def max_subarray(self, nums) -> int:
        if not nums:
            return 0

        max_subsum_ends_here = nums[0]
        max_subsum = nums[0]

        for i in range(1, len(nums)):
            max_subsum_ends_here = nums[i] if max_subsum_ends_here <= 0 else max_subsum_ends_here + nums[i]
            max_subsum = max(max_subsum, max_subsum_ends_here)

        return max_subsum
