num1 = int(input("number1 is?\n"))

num2 = int(input("number 2 is?\n"))

verschil = num2 - num1
if verschil < 0:
    verschil = verschil * -1

if verschil < 5:
    print("kleiner")
else:
    print("groter")
