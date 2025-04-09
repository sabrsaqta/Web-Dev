def make_bricks(small, big, goal):
  while goal > 5 and big > 0:
    goal -= 5
    big -= 1
  
  if goal == 0:
    return True
  elif goal == 5 and big > 0:
    return True
  elif goal <= small:
    return True
  else:
    return False
