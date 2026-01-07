password = input("masukan password anda :")
panjang = len(password)

if panjang < 8:
    print("password kurang dari 8 karakter")
else :
    print("password berhasil")