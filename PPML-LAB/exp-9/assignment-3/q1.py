#wap to print twin prime numbers between 1 to N

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter N: "))

print("Twin prime numbers between 1 and", n, "are:")

for i in range(2, n-1):
    if is_prime(i) and is_prime(i+2):
        print(i, i+2)