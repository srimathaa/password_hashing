

## 📂 Project Structure

# 🔐 Password Hashing Login System (Beginner Cybersecurity Project)

This is a **beginner-level cybersecurity project** that demonstrates how a **secure login system** works using **password hashing** instead of storing plain passwords.

---

## 📌 Project Objective

- Show why **plain text passwords are insecure**
- Learn how **password hashing** works
- Understand **basic authentication flow** (Register → Login)

---

## 🧠 Key Cybersecurity Concepts Used

- Password Hashing (SHA-256)
- Authentication Basics
- Secure Password Storage
- File-based User Database

---

## 🛠️ Technologies Used

- Python
- `hashlib` (built-in Python library)
- Text file (`users.txt`) as a simple database

---

## 📂 Project Structure


---

## 🔄 How the System Works

### 📝 Registration
1. User enters username and password
2. Password is converted into a **hash**
3. Username and hashed password are saved

### 🔐 Login
1. User enters username and password
2. Entered password is hashed again
3. Hash is compared with stored hash
4. If they match → Login successful ✅

---

## ▶️ How to Run the Project

### Step 1: Register a user
```bash
### python register.py
Step 2: Login
python login.py
