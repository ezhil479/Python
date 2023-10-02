price = {"apple":25 , "orange":15 , "banana":8 }
total = 0
for i in range(3):
  fruit = input("Enter fruit name: ")
  quantity = input("Enter the quantity: ")
  quantity = int(quantity)
  
  subtotal = price[fruit] * quantity
  total = total + subtotal

print(total)  