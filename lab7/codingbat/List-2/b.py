# def count_evens(nums):
#   cnt = 0
#   for i in nums:
#     if i % 2 == 0:
#       cnt += 1
      
#   return cnt

def big_diff(nums):
  maxn = nums[0]
  minn = nums[0]
  for i in range(len(nums)-1):
    maxn = max(maxn, nums[i+1])
    minn = min(minn, nums[i+1])
  return maxn-minn
