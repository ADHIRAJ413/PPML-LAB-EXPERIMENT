#wap to create a function that prints the first 14 terms of the fibonnaci series without using recursion.

def fibonnaci(n):
    a=0
    b=1
    print(a,b,end="")
    #print(b)
    for i in range(2,n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
n=int(input("Enter the number of terms you want to print:"))
print("The fibonnaci series of first",n,"terms are:")
fibonnaci(n)