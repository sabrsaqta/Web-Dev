def count_hi(str):
  cnt = 0
  for i in range(len(str)-1):
    str2 = str[i] + str[i+1]
    if str2 == "hi":
      cnt += 1
  return cnt
