def count_code(str):
  cnt = 0
  for i in range(len(str)-3):
    if str[i] + str[i+1] == "co" and str[i+3] == 'e':
      cnt += 1
  return cnt
