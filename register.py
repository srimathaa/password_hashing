import hashlib

username = input("Enter username: ")
password = input("Enter password: ")

# convert password to hash
hashed_password = hashlib.sha256(password.encode()).hexdigest()

# save to file
with open("users.txt", "a") as file:
    file.write(username + "," + hashed_password + "\n")

print("User registered successfully!")
