# Day 3 Wisdom training

# continue
"""for i in range(5):
    if i == 3:
        continue
    print("This is continue")"""

# String operations
"""var = "good"
print(var.count('o'))"""

# split()
"""var = "I am Value python"
print(var.split('a'))"""

# 
"""var = "I am Value python check a 2 only"
print(var.split('a',2))"""

# name format string
"""name = input("Enter name: ")
mark = int(input("Enter mark: "))

if mark >= 50:
    print(f"{name} is pass...")
else:
    print(f"{name} is fail...")"""


# split name and mark using :
"""details = input("Enter name and mark: ")

details_list = details.split(":")

name = details_list[0]
mark = details_list[1]
mark = int(mark)

if mark >= 50:
    print(f"{name} you are pass, mark is {mark}")
else:
    print(f"{name} you are fail, mark is {mark}")"""


# splitlines operation
"""
var = """ #hi how are you
#i am fine
#how about you
#i am good
"""
print(var.splitlines())
"""
# use for loop in splitlines
"""
#var =  hi python how are you
i am fine
how python about you
i am good
"""
"""var2 = var.splitlines()

for line in var2:
    if 'python' in line:
        print(line)
"""

# take particular fail id
#var = 
"""TC_1 is pass
TC_2 is fail
TC_3 is pass
TC_4 is pass
TC_5 is fail
"""

"""for i in var.splitlines():
    if "fail" in i:
        print(i.split()[0])"""

# join
"""list1 = ['a','b','c','d']

var = '.'.join(list1)
print(var)"""

# ascending
"""var = [78,99,98,45,3,23,1]
var.sort()
print(var)"""

# descending
"""var = [78,99,98,45,3,23,1]
var.sort(reverse=True)
print(var)"""

# print mark

list1 = [] # empty list

sub = ['Tamil', 'English', 'Maths','Science','SocialScience']

result = "Pass"
for i in sub:
    mark = input(f"Enter mark of {i}: ")
    mark = int(mark)
    if mark <= 50:
        result = "Fail"
    list1.append(mark)    

total = sum(list1)

avg = total / len(list1)

print(f"total is {total}, average is {avg}, result is {result}")


