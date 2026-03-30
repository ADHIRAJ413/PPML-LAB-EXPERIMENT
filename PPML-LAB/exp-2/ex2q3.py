l=[]
print("Enter five fruits name:")
for i in range (0,5):
    l.append(input())
    print("The entered fruits are:",end=" ")
for i in range(0,5):
    print(l[i],end=",")