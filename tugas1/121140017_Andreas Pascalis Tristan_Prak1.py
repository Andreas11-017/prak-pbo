n = int(input("Masukkan n : "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

for enter in range(2):
    print()

for x in range(1, 4):
    username = input("Username anda : ")
    password = int(input("Password anda : "))

    if username == "informatika" and password == 12345678:
        print("Berhasil login!")
        break
    elif x == 3 and (username != "informatika" or password != 12345678):
        print("You've ran out of chances my friend")
    elif username != "informatika" or password != 12345678:
        print("Username atau password anda salah coba lagi")

