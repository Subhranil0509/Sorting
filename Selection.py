list = [87,32,21,54,99,1,4,73,12]
n = len(list)
print(list)
for i in range(n):
  minpos=i
  for j in range(i,n):
    if list[j]<list[minpos]:
      minpos=j
  list[i],list[minpos] = list[minpos],list[i]
print(list)