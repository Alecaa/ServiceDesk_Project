import bcrypt

password = bcrypt.hashpw("123456".encode(), bcrypt.gensalt())
print(password.decode())