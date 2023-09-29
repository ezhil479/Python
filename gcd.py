# GCD/HCF = Greatest Common Divisor/Highest Common Factor

def hcf(x,y):
    global a
    a = []
    count = 0

    if x>y:
        small=y 
    else:
        small=x
    for i in range(1,small+1):
        if((x%i == 0) and (y%i == 0)):
            count = count+1
            a.append(i)
    return count

a = int(input("Enter first value: "))         
b = int(input("Enter second value: "))
c = hcf(a,b)

print("HCF value is: ",c)
print("HCF count is: ",a)
