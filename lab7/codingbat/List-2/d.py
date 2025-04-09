def thesum(nums):
    if len(nums) == 0:
        return 0
    sum = 0
    for i in range(len(nums)):
        if nums[i] == 14 or nums[i-1] == 14:
            continue
        else:
            sum += nums[i]
    return sum


nums = []

print(thesum(nums))