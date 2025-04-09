def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if a in b:
    if b[-len(a):] == a:
      return True
  if b in a:
    if a[-len(b):] == b:
      return True
  return False
