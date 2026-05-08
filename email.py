email = str(input("Enter your email: "))
count = email.count("@")
if "@" in email:
    email.count("@")
    if count == 1:
        user_name , domain = email.split("@")
    if "." in domain:
        print(f"A Email has both {user_name} and {domain} ,so which is valid")
    else:
        print("Invalid")
else:
    print("Pls enter a valid emaill")
