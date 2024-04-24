userInput = int(input("Enter your money: "))
value = int(input("How much is it: "))
remainder = userInput - value
fiveHundreds = remainder // 500
oneHundreds = (remainder % 500) // 100
print(fiveHundreds, oneHundreds)