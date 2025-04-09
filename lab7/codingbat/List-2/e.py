def sum67(nums):
  sum = 0
  skip = False
  for i in range(len(nums)):
    if nums[i] == 6:
      skip = True
    if not skip:
      sum += nums[i]
    if skip == True and nums[i] == 7:
      skip = False
  return sum
