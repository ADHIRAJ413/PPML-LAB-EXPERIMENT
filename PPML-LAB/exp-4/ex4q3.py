a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))

gcd = 1
i = 1

while i <= a and i <= b and i <= c:
    if a % i == 0 and b % i == 0 and c % i == 0:
        gcd = i
    i = i + 1

print("GCD of three numbers:", gcd)
