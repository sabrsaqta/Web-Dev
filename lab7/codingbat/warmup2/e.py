def last2(str):
  fragment = str[len(str)-2:len(str)]
  cnt = 0
  for i in range(1, len(str)-1):
    x = str[i-1] + str[i]
    if x == fragment:
      cnt += 1
  return cnt