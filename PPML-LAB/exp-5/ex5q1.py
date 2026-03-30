n = int(input("Enter n: "))

a = 0
b = 1
i = 0

while i < n:
    if a % 2 == 0:
        print(a, end=" ")
    a, b = b, a + b
    i += 1
