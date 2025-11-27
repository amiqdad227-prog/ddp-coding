import bangun_datar, bangun_ruang

print("====Luas Bangun Datar====")
print(f"Luas persegi = {bangun_datar.luas_persegi(5)}")
print(f"Luas segitiga = {bangun_datar.luas_segitiga(5, 5)}")
print(f"Luas lingkaran = {bangun_datar.luas_lingkaran(5)}")
print(f"Luas ketupat = {bangun_datar.luas_ketupat(5,5)}")
print(f"Luas jajar genjang = {bangun_datar.luas_jajar_genjang(5,5)}")


print("====Luas Bangun Ruang====")
print(f"Luas Kubus = {bangun_ruang.luas_kubus(3)}")
print(f"Luas Balok = {bangun_ruang.luas_balok(4, 5, 7)}")
print(f"Luas Bola = {bangun_ruang.luas_bola(2)}")
print(f"Luas Tabung = {bangun_ruang.luas_tabung(1, 10)}")
print(f"Luas Kerucut = {bangun_ruang.luas_kerucut(1, 4)}")
