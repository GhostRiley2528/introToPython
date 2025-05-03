import random
import string
import time
import math
import datetime
import os

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def check_strength(password):
    length_score = min(len(password) / 8, 1)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    score = length_score + has_upper + has_lower + has_digit + has_special
    return score

print("🔐 Password Strength Checker")
password = input("Enter your password (or leave blank to generate one): ")

if not password:
    length = int(input("Enter desired password length: "))
    password = generate_password(length)
    print("Generated password:", password)

strength = check_strength(password)

print("\nChecking strength", end="")
for _ in range(3):
    print(".", end="")
    time.sleep(0.5)
print()

if strength >= 4.5:
    print("✅ Strong password!")
elif strength >= 3:
    print("⚠️ Medium strength password. Consider making it longer or more complex.")
else:
    print("❌ Weak password! Try adding symbols, numbers, and uppercase letters.")

# Bonus: save password with timestamp (optional)
save = input("\nSave this password to a file? (y/n): ").lower()
if save == 'y':
    filename = "saved_passwords.txt"
    with open(filename, "a") as f:
        f.write(f"{datetime.datetime.now()}: {password}\n")
    print(f"Password saved to {os.path.abspath(filename)}")
