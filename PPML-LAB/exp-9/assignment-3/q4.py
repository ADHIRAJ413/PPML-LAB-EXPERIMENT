#wap to check wheather the string is symmetrical or plindrome.

x=input("enter a string")
z=(str(str(x)[::-1]))
if x==z:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
