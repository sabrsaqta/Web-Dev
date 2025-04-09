def xyz_there(str):
  flag = True
  if "xyz" in str:
    for i in range(len(str)-3):
      if str[i] == '.' and str[i+1:i+4] == "xyz":
        flag = False
        if "xyz" in str[i+3:]:
          flag = True
          
  else:
    flag = False
  return flag
