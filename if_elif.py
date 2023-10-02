num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

opr = input("Enter the Operation add, sub, mul, div: ")

if opr == "add":
  total = num1 + num2
  print(total)
elif opr == "sub":
  total = num1 - num2
  print(total)
elif opr == "mul":
  total = num1 * num2
  print(total)
elif opr == "div":
  total = num1 / num2
  print(total)
else:
  print("Please choose the correct option...")