#wap to calculate factorial of a number using recursion.

def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result

n = int(input("Enter a number: "))
if(n<0):
    print("It is a Negative number:")
else:
    print("Factorial of", n, "is:", factorial(n))