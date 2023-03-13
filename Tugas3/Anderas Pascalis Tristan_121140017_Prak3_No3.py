"""
Buatlah demonstrasi kelas (topik dan konsep bebas) yang dapat memperlihatkan perbedaan
antara atribut/fungsi private, protected, dan public secara jelas (kapan atribut private harus
digunakan, kapan atribut public harus digunakan, dsb). Gunakan juga konsep atribut/fungsi
kelas (yaitu atribut/fungsi yang bernilai konsisten antar instance) bila memungkinkan untuk
mendukung demonstrasi yang Anda buat.

Nama : Andreas Pascalis Tristan
NIM : 121140017
Kelas : RB
"""


class Karyawan:
    department = "Marketing"  # ini class attribute

    def __init__(self, nama, umur, gaji):
        self.nama = nama  # sebagai public attribute
        self._umur = umur  # sebagai protected attribute
        self.__gaji = gaji  # bersifat private attribute

    def tampilkan_nama(self):  # public method
        print(self.nama)

    def _tampilkan_umur(self):  # protected method
        print(self._umur)

    def __tampilkan_gaji(self):  # private method
        print(self.__gaji)

    def tampilkan_gaji_public(self):  # public method yang membungkus private method (enkapsulasi)
        Karyawan.__tampilkan_gaji(self)  # private method bisa di akses dalam kelas

    def get_gaji(self):  # getter method
        return self.__gaji

    def set_gaji(self, gaji_baru):  # setter method
        self.__gaji = gaji_baru

    @property  # decorator
    def gaji(self):  # bentuk getter dari decorator
        return self.__gaji

    @gaji.setter  # decorator
    def gaji(self, gaji_baru):  # bentuk setter dari decorator
        self.__gaji = gaji_baru


class turunan(Karyawan):  # inheritance
    def __init__(self, nama, umur, gaji):
        super().__init__(nama, umur, gaji)

    def get_umur(self):
        return Karyawan._tampilkan_umur(self)  # protected method bisa diakses di kelas turunan

    def get_gaji(self):
        return Karyawan.__tampilkan_gaji(self)  # private method tidak bisa diakses di kelas turunan


karyawan1 = Karyawan("Budik", 32, 3_000_000)  # objek baru dari class Pekerja

print(karyawan1.nama)  # public attribute bisa diakses di luar kelas
print(karyawan1._umur)  # protected attribute bisa diakses di luar kelas
# print(pekerja1.__gaji) # private attribute tidak bisa diakses di luar kelas
print(karyawan1._Karyawan__gaji)  # private attribute bisa diakses secara paksa dengan menambahkan _class
print(karyawan1.get_gaji())  # private attribute bisa diakses di luar kelas menggunakan getter method (public method)
print()

karyawan1.tampilkan_nama()  # public method bisa di akses di luar kelas
karyawan1._tampilkan_umur()  # protected method bisa di akses di luar kelas
# pekerja1.__tampilkan_gaji() # private method tidak bisa di akses di luar kelas
karyawan1._Karyawan__tampilkan_gaji()  # private method bisa diakses secara paksa dengan menambahkan _class
karyawan1.tampilkan_gaji_public()  # private method dapat dibungkus dengan public method agar bisa digunakan di luar kelas
print()

karyawan1.nama = "Bobon"  # public attribute bisa diubah di luar kelas
print(karyawan1.nama)
karyawan1._umur = 28  # protected attribute bisa diubah di luar kelas
print(karyawan1._umur)
karyawan1.__gaji = 1_000_000  # private attribute tidak bisa diubah di luar kelas
print(karyawan1.get_gaji())  # syntax line 38 tidak mengubah private attribute gaji
karyawan1.set_gaji(1_000_000)  # private attribute dapat diubah dengan bantuan setter method (public method)
print(karyawan1.get_gaji())
print()

print(karyawan1.gaji)  # private attribute dapat diakses karena sudah dibuat getter decoratornya
karyawan1.gaji = 3_000_000  # private attribute dapat diubah karena sudah dibuat setter decoratornya
print(karyawan1.gaji)
print()

# fungsi dari decorator adalah untuk mempermudah pemanggilan method dari suatu kelas, karena nama method getter dan setternya bisa sama
# dalam python protected dan public attribute tidak terlalu berbeda

karyawan2 = turunan("Udin", 20, 3_000)
karyawan2.get_umur()
# pekerja2.get_gaji() # tidak bisa mengakses public method karena terdapat private method
print()

contoh_1 = Karyawan("Mamat", 30, 1_000)
contoh_2 = Karyawan("Cecep", 40, 2_000)
print(contoh_1.department)  # nilai class attribute konstan
print(contoh_2.department)  # nilai class attribute konstan