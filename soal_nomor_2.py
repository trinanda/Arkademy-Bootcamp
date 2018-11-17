import re

def validate():
    while True:
        password = input("Enter a password: ")
        if len(password) < 8:
            print("Minimal karakter untuk password nya adalah 8")
        elif re.search('[@#$%^&+=_.-]',password) is None:
            print("Pola yang di masukan salah, mohon diulangi!")
        elif re.search('[A-Z]', password) is None:
            print("Pola yang di masukan salah, mohon diulangi!")
        elif re.search('[a-z]', password) is None:
            print("Pola yang di masukan salah, mohon diulangi!")
        else:
            print("Sukses")
            break

validate()