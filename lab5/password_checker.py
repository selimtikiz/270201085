static_password = "abc123"

while True:
    password = input("enter the password")
    if password == "help":
        print(static_password[0])

    elif password == static_password:
        print("welcome")
        break
    else:
        print("wrong")



