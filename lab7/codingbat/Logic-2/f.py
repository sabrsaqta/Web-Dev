def close_far(a, b, c):
  if abs(abs(a) - abs(b)) <= 1:
    if abs(a - c) >= 2 and abs(b-c) >= 2:
      return True
  if abs(abs(a) - abs(c)) <= 1:
    if abs(a - b) >= 2 and abs(c - b) >= 2:
      return True
  return False
    
