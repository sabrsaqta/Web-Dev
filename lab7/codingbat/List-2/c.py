def centered_average(nums):
  maxn = max(nums)
  minn = min(nums)
  wasMax = False
  wasMin = False
  
  cnt = 0
  sum = 0
  for i in nums:
    if i == maxn:
      if not wasMax:
        wasMax = True
        continue
      else:
        sum += i
        cnt += 1
    elif i == minn:
      if not wasMin:
        wasMin = True
        continue
      else:
        sum += i
        cnt += 1
    else:
      sum += i
      cnt += 1
  res = sum // cnt
  return res