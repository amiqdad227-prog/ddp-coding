# Module: baking_calculator.py
recipes = {
    "brownies": {"tepung": 200, "gula": 150, "telur": 3, "coklat": 100},
    "cookies": {"tepung": 250, "gula": 100, "telur": 2, "mentega": 150},
    "pancake": {"tepung": 180, "gula": 50, "telur": 2, "susu": 200}
}

def calculate_ingredients(recipe_name, multiplier):
    """Function hitung bahan dengan multiplier"""
    if recipe_name in recipes:
        result = {}
        # Looping melalui bahan
        for ingredient, amount in recipes[recipe_name].items():
            result[ingredient] = amount * multiplier
        return result
    return None

def main():
    while True:
        print("\n=== KALKULATOR BAHAN KUE ===")
        print("1. Hitung Bahan")
        print("2. Lihat Resep")
        print("3. Keluar")
        
        choice = input("Pilih menu: ")
        
        if choice == "1":
            # Page: Hitung bahan
            print("\nPilih resep:")
            # Looping untuk tampilkan pilihan resep
            recipes_list = list(recipes.keys())
            for i, recipe in enumerate(recipes_list, 1):
                print(f"{i}. {recipe.capitalize()}")
            
            try:
                recipe_choice = int(input("Pilihan resep: ")) - 1
                multiplier = float(input("Jumlah batch: "))
                
                if 0 <= recipe_choice < len(recipes_list):
                    recipe_name = recipes_list[recipe_choice]
                    ingredients = calculate_ingredients(recipe_name, multiplier)
                    
                    if ingredients:
                        print(f"\n=== BAHAN UNTUK {multiplier} BATCH {recipe_name.upper()} ===")
                        # Looping tampilkan bahan
                        for ingredient, amount in ingredients.items():
                            print(f"- {ingredient}: {amount} gram")
                    else:
                        print("Resep tidak ditemukan!")
                else:
                    print("Pilihan tidak valid!")
                    
            except ValueError:
                print("Input harus angka!")
                
        elif choice == "2":
            # Page: Lihat resep
            print("\n=== RESEP YANG TERSEDIA ===")
            # Looping melalui semua resep
            for recipe_name, ingredients in recipes.items():
                print(f"\n{recipe_name.upper()}:")
                for ingredient, amount in ingredients.items():
                    print(f"  - {ingredient}: {amount} gram")
                    
        elif choice == "3":
            break
            
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()