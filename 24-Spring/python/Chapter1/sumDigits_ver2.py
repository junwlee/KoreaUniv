total = 0
num = int(input("Enter a number: "))
while num > 0:
    total += num % 10
    num = num // 10

print(total)