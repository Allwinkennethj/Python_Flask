import bcrypt

def hash_password(password):
    password_hash=bcrypt.hashpw(password=password.encode("utf8"),salt=bcrypt.gensalt())
    return password_hash.decode("utf8")

def check_passoword(new_password,exist_password):
    return bcrypt.checkpw(new_password,exist_password)