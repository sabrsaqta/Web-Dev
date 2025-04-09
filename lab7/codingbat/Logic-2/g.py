def make_chocolate(small, big, goal):
  if small + big*5 < goal:
    return -1
  
  big_used = goal // 5
  if big_used > big:
    big_used = big
  goal -= big_used * 5
  if goal <= small or goal == 0:
    return goal
  return -1