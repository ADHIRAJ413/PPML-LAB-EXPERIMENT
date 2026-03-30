#def sum(n):
#    if n%2==0:
#        return n
#    else:
#        return 0
#
#num=int(input("eneter the number"))
#print("even  number ",sum(num))
#def sum(a,b):
#    return a+b
#print("sum  of two number",sum(4,5))
#def factorial(n):
# fact=1
# for i in range(1,n+1):
#        fact= fact*i
#        
# return fact      
#
#print("factorial",factorial(n=6))
#def revstr(n):
#    count=0
#    for i in n:
#        if i in "a,e,i,o,u":
#         count=count+1
#    return count              
#            
#
#num=str(input("enter the string"))
#print("revers ethe string :", revstr(num))
def large(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and  b>c:
        return b
    else:
        return c
print("large number  :", large(a=5,b=3,c=2))  