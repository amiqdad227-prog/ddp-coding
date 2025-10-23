print("program menghitung luas bangun datar")
print("1. persegi")
print("2. lingkarang")
print("3. segitiga")

hitung =int(input("memilih program (1/2/3):"))

match hitung:
    case 1:
        sisi = float(input("masukan panjang sisi:"))
        luas = sisi * sisi
        print(luas)
    case 2:
        r = float(input("masukan jari-jari lingkaran;"))
        luas = 3.14 * r * r
        print(luas)
    case 3:
        alas = float(input("masukan alas segitiga:"))
        tinggi = float(input("masukan tinggi segitiga:"))
        luas = 0.5*alas*tinggi
        print(luas)
    case _:
        print("SALAH PILIH")
