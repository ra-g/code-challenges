def find_pivot(l):
  s = 0
  e = len(l) - 1
  m = (s + e) // 2
  if l[s] < l[e]:
    return len(l) - 1
  while (s != e):
    if l[s] < l[m]:
      s = m
    else:
      e = m
    m = (s + e) // 2
  return s

#iterative
def binarysearch(l,x):
  s = 0
  e = len(l) - 1
  while (s<=e):
    m = (s+e) // 2
    if l[m] == x:
      return m
    elif l[m] > x:
      e = m-1
    else:
      s = m+1
  return None

def find_val(l,val):
  pivot = find_pivot(l) 
  if val == l[pivot]:
    return pivot
  if l[0] <= val < l[pivot]:
    return binarysearch(l[0:pivot],val)
  elif l[pivot+1] <= val <= l[-1]:
    return pivot + 1 + binarysearch(l[pivot+1:],val)
  return None

my_list = [5, 6, 7, 8, 9, 10, 1, 2, 3]
print ("value is at index", find_val(my_list,3))
