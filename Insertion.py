list = [5,3,4,2,6,9,1]
n = len(list)
print("The list: ",end="")
print(list)
for i in range (1,n):
    j=i
    while list[j-1]>list[j] and j>0:
      list[j-1],list[j]=list[j],list[j-1]
      j=j-1
print ("Shotted list:",end=" ")
print(list)
