def round_sum(a, b, c):
  sum = 0
  sum += round10(a)
  sum += round10(b)
  sum += round10(c)
  return sum
  
  
def round10(num):
  if num % 10 >= 5:
    num += (10-(num%10))
  else:
    num -= (num%10)
  return num