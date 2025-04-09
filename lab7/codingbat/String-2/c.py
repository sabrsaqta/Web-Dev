def cat_dog(str):
  cat = 0
  dog = 0
  for i in range(len(str)-2):
    str2 = str[i] + str[i+1] + str[i+2]
    if str2 == "cat":
      cat += 1
    elif str2 == "dog":
      dog += 1
  if cat == dog:
    return True
  return False