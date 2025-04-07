def near_ten(num):
  if abs(num % 10 - 10) <= 2 or num % 10 <= 2:
    return True
  return False
