jumlah = int(input("jumlah pembelian:"))

total = jumlah *0.9 if jumlah > 100 else jumlah 
print(f"total yg dibayar: {total}")