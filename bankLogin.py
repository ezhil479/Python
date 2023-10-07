users = {"admin":"simple","root":"abcd","skumar":"goodman"}

for i in range(3):
    user_name = input("Enter username: ")
    password = input("Enter password: ")

    if users[user_name] == password:
        print("You are welcome...")
        break
    else:
        if i != 2:
            print("Your password is wrong please re-try.")

else:
    print("Your password wrong, account blocked")