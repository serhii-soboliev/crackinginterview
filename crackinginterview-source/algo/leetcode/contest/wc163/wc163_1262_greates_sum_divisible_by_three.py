class GreatestSumDivisibleByThree:

    def max_sum_div_three(self, nums) -> int:
        sums = [0,0,0]
        for n in nums:
            new_sums = [sums[0] + n, sums[1] + n, sums[2] + n]
            for new_sum in new_sums:
                m = new_sum % 3
                sums[m] = max(sums[m], new_sum)
        return sums[0]