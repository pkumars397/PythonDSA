def moveZeroes( nums: list[int]) -> None:
        nonzero, i = 0, 0  # Initialize pointers
        n = len(nums)
        while i < n:
            if nums[i] != 0:
                # Swap non-zero element with the element at the `nonzero` pointer
                nums[i], nums[nonzero] = nums[nonzero], nums[i]
                nonzero += 1  # Move `nonzero` pointer
            i += 1  # Move `i` pointer

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)
