# DISARIUM -The sum of the digit raised to the power of their respective positions becomes 
#  equal to the number itself.

# 175 = 1^1 + 7^2 + 5^3 = 1+49+125 = 175

num = int(input("Enter num: "))
ans = 0
count = 1
numstring = str(num)

for char in numstring:
    ans = ans + int(char)**count
    count = count+1

if (num == ans)    :
    print("Num is disarium ",num)
else:
    print(num," is not a disarium")    