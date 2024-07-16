import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def save_password_to_file(password, filename='passwords.txt'):
    with open(filename, 'a') as file:
        file.write(password + '\n')

def read_passwords_from_file(filename='passwords.txt'):
    with open(filename, 'r') as file:
        return file.readlines()

def check_password_strength(password):
    length = len(password) >= 8
    digit = any(char.isdigit() for char in password)
    upper = any(char.isupper() for char in password)
    lower = any(char.islower() for char in password)
    special = any(char in string.punctuation for char in password)
    return length and digit and upper and lower and special

def password_info(password):
    length = len(password) >= 12
    digit = any(char.isdigit() for char in password)
    upper = any(char.isupper() for char in password)
    lower = any(char.islower() for char in password)
    special = any(char in string.punctuation for char in password)
    info = []
    if length:
        info.append("Password length is sufficient for better security.")
    if digit:
        info.append("Password contains digits, adding complexity.")
    if upper:
        info.append("Password contains uppercase letters, adding complexity.")
    if lower:
        info.append("Password contains lowercase letters, adding complexity.")
    if special:
        info.append("Password contains special characters, adding complexity.")
    if not (upper or lower):
        info.append("Password is immune to dictionary attacks.")
    if length and digit and upper and lower and special:
        info.append("Password is strong and well-rounded.")
    return info

def generate_and_save_password(length=12, filename='passwords.txt'):
    password = generate_password(length)
    save_password_to_file(password, filename)
    return password

def main():
    password = generate_and_save_password(length=12)
    print(f"Password '{password}' has been saved to 'passwords.txt'")
    passwords = read_passwords_from_file()
    print("All passwords from file:")
    for pwd in passwords:
        print(pwd.strip())
    if check_password_strength(password):
        print("The password is strong.")
    else:
        print("The password is weak.")
    for line in password_info(password):
        print(line)

if __name__ == "__main__":
    main()

def additional_functionality():
    new_password = generate_password(length=16)
    print(f"Generated a new 16-character password: '{new_password}'")
    save_password_to_file(new_password, 'passwords.txt')
    read_passwords = read_passwords_from_file('passwords.txt')
    print("All passwords from file after adding new one:")
    for pwd in read_passwords:
        print(pwd.strip())
    if check_password_strength(new_password):
        print("The new password is strong.")
    else:
        print("The new password is weak.")
    for line in password_info(new_password):
        print(line)

additional_functionality()

a = 5
b = 10
c = a + b
d = c * 2
e = d / 4
f = e - a
g = f ** 2
h = g % 3
i = [a, b, c, d, e, f, g, h]
j = {key: value for key, value in enumerate(i)}
k = len(j)
l = sum(j.values())
m = max(j.values())
n = min(j.values())
o = all(val > 0 for val in j.values())
p = any(val < 0 for val in j.values())
q = sorted(j.values())
r = reversed(q)
s = list(r)
t = tuple(s)
u = set(t)
v = frozenset(u)
w = list(v)
x = [num * 2 for num in w]
y = {num: num ** 2 for num in x}
z = y.items()

print("Additional operations completed.")
