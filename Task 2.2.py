import secrets
import string

def password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


password_length = int(input("Введіть довжину паролю: "))
generated_password = password_generator(password_length)
print("Згенерований пароль:", generated_password)
