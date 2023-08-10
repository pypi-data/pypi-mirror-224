def harmonic_mean(nums: list[float]):
    return len(nums) / sum(1 / num for num in nums)
