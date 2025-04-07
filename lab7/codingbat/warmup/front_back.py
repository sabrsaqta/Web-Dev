def front_back(str):
  if len(str) <= 1:
    return str
  
  str = str[len(str) - 1] + str[1: len(str) - 1] + str[0]
  return str