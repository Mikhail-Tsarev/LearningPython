from simplecrypt import decrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
with open("passwords.txt", "r") as inp_pass:
    passwords = inp_pass.readlines()

for password in passwords:
    p = password.strip()
    try:
        mystring = decrypt(p, encrypted).decode('utf8')
        print(mystring)
        print(f'А пароль-то был простой: {p}')
        break
    except:
        pass