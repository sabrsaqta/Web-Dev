def caught_speeding(speed, iss):
  if iss:
    if speed <= 65:
      return 0
    elif speed in range(66, 86):
      return 1
    else: return 2
  else:
    if speed <= 60:
      return 0
    elif speed in range(61, 81):
      return 1
    else: return 2
