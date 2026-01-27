import hashlib

username = input("Enter username: ")
password = input("Enter password: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

login_success = False

with open("users.txt", "r") as file:
    for line in file:
        stored_username, stored_hash = line.strip().split(",")

        if stored_username == username and stored_hash == hashed_password:
            login_success = True
            break

if login_success:
    print("Login successful ✅")
else:
    print("Login failed ❌")
