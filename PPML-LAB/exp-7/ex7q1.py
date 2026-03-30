m=int(input("enetr the m"))
n=int(input("enetr the m"))
number=[]
for i in range(m,n+1):
    number.append(i)
print("list :",number)    
total=sum(number)
print(total)
avg=total/len(number)
print(avg)
print(max(number),min(number))
l=[]
for num in number:
    if num%3!=0:
        l.append(num)
print(l)        