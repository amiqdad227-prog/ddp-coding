
inventory = ["pedang", "perisai", "roti"]

 
perintah = input("Perintah: ").split()

 
match perintah[0]:
    case "ambil":
        if len(perintah) > 1:
            item = perintah[1]
            inventory.append(item)
            print(f"Kamu mengambil {item}.")
        else:
            print("Kamu harus menyebutkan apa yang ingin diambil.")
    case "buang":
        if len(perintah) > 1:
            item = perintah[1]
            if item in inventory:
                inventory.remove(item)
                print(f"Kamu membuang {item}.")
            else:
                print(f"Tidak ada {item} di inventory.")
        else:
            print("Kamu harus menyebutkan apa yang ingin dibuang.")
    case "lihat":
        print(f"Inventory kamu: {inventory}")
    case _:
        print("Perintah tidak dikenal.")

 
print(f"Inventory akhir: {inventory}")