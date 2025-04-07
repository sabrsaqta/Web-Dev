def squirrel_play(temp, is_summer):
  if is_summer:
    if temp in range(60, 101):
      return True
    else: return False
  else:
    if temp in range(60, 91):
      return True
  return False
