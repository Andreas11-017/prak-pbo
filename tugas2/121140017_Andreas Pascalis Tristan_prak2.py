class mahasiswa: #ini kelas
    def __init__(self, nama, NIM, kelas_siakad, jumlah_sks): #ini atribut
        self.nama = nama
        self.NIM = NIM
        self.kelas_siakad = kelas_siakad
        self.sks = jumlah_sks

    def panggil_data(self): #ini konstruktor
        print("Nama : ", self.nama)
        print("NIM : ", self.NIM)
        print("Kelas PBO : ", self.kelas_siakad)
        print("Jumlah SKS : ", self.sks)

andreas = mahasiswa("Andreas", 121140017, "RB", 20) #input
andreas.panggil_data() #pemaggilan
