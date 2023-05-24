list = [87,32,21,54,99,1,4,73,12]
n = len(list)
print("The list: ",end="")
print(list)
for i in range(0,n):
  for j in range(0,n-i-1):
    if list[j]>list[j+1]:
      list[j+1],list[j] = list[j],list[j+1]

print ("Shotted list:",end=" ")
print(list)