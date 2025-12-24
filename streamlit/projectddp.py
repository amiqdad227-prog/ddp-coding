import streamlit as st
class Resep:
    def __init__(self, nama, waktu, bahan, rating, gambar_url, cara_memasak):
        self.nama = nama
        self.waktu = waktu
        self.bahan = bahan
        self.rating = rating
        self.gambar_url = gambar_url
        self.cara_memasak = cara_memasak
    
    def to_dict(self):
        return {
            "nama": self.nama,
            "waktu": self.waktu,
            "bahan": self.bahan,
            "rating": self.rating,
            "gambar_url": self.gambar_url,
            "cara_memasak": self.cara_memasak
        }

if "resep" not in st.session_state:
    st.session_state.resep = [
        {"nama": "Brownies🍪", "waktu": 45, "bahan": ["100g mentega","200g dark coklat", "2 telur", "150g gula putih",
                                                       "100g tepung terigu", "1 sdt garam", "40g cocoa powder"], "rating": 5,
         "gambar_url": "https://i.pinimg.com/1200x/f8/01/2b/f8012bd5959e5cd1ae8ab6489cd42bde.jpg",
         "cara_memasak": [
             "Lelehkan mentega dan dark coklat dengan cara di-tim hingga tercampur rata",
             "Kocok telur dan gula putih hingga mengembang dan pucat",
             "Campurkan lelehan coklat ke dalam adonan telur, aduk rata",
             "Ayak tepung terigu, garam, dan cocoa powder, lalu masukkan ke adonan",
             "Tuang adonan ke loyang yang sudah diolesi mentega",
             "Panggang dalam oven suhu 180°C selama 30-35 menit",
             "Dinginkan sebelum dipotong"
         ]},
        {"nama": "Nastar🍍", "waktu": 60, "bahan": ["270g tepung terigu", "50g gula halus", "1 telur", "26g susu bubuk",
                                                     "30g tepung maizena", "200g mentega", "7g selai nanas"], "rating": 4,
         "gambar_url": "https://i.pinimg.com/1200x/2e/ce/47/2ece4754768daf3bc83003c8d0a57ca8.jpg",
         "cara_memasak": [
             "Kocok mentega dan gula halus hingga lembut dan pucat",
             "Masukkan telur kuning, aduk rata",
             "Ayak tepung terigu, maizena, dan susu bubuk",
             "Campurkan tepung ke dalam adonan mentega, aduk hingga kalis",
             "Ambil sedikit adonan, pipihkan, isi dengan selai nanas, bentuk bulat",
             "Olesi kuning telur di atas nastar",
             "Panggang dalam oven suhu 150°C selama 20-25 menit hingga kekuningan"
         ]},
        {"nama": "Donat🍩", "waktu": 30, "bahan": ["20 sdm tepung terigu tinggi protein", "3 sdm gula", "1 telur", "2 sdm susu bubuk",
                                                     "3g ragi", "130ml susu cair", "7g selai strawberry", "2 sdm baking powder"], "rating": 4.5,
         "gambar_url": "https://i.pinimg.com/1200x/bd/2a/d3/bd2ad383d46ee07b06971675081a2e5d.jpg",
         "cara_memasak": [
             "Campurkan tepung terigu, gula, susu bubuk, baking powder, dan ragi",
             "Tambahkan telur dan susu cair sedikit demi sedikit sambil diuleni",
             "Uleni adonan hingga kalis dan elastis",
             "Diamkan adonan selama 30 menit hingga mengembang",
             "Bentuk adonan menjadi bulat dengan lubang di tengah",
             "Goreng dalam minyak panas dengan api sedang hingga kecoklatan",
             "Tiriskan dan beri topping sesuai selera (gula halus/selai/coklat)"
         ]},
        {"nama": "Waffle🧇", "waktu": 10, "bahan": ["7 sdm tepung terigu rendah protein", "1 sdm baking powder", "1 telur kuning", "1 sdm susu bubuk",
                                                     "100ml susu cair", "2 sdm minyak", "5 sdm saus caramel", "2 buah strawberry"], "rating": 5,
         "gambar_url": "https://i.pinimg.com/1200x/f1/1f/97/f11f976b0a79142bdd6e05728fa43eba.jpg",
         "cara_memasak": [
             "Campurkan tepung terigu, baking powder, dan susu bubuk",
             "Kocok telur kuning hingga berbusa",
             "Tambahkan susu cair dan minyak ke dalam telur, aduk rata",
             "Masukkan campuran tepung ke adonan basah, aduk hingga tercampur",
             "Panaskan cetakan waffle, olesi sedikit mentega",
             "Tuang adonan ke cetakan, masak hingga kecoklatan (3-5 menit)",
             "Sajikan dengan saus caramel dan potongan strawberry"
         ]},
        {"nama": "Apple Pie🥧", "waktu": 25, "bahan": ["133g tepung terigu", "1,5 sdm baking powder", "1 telur kuning", "15g gula halus",
                                                     "75g margarin", "1 sdm air dingin", "3 buah apel", "1 sdm brown sugar"], "rating": 5,
         "gambar_url": "https://i.pinimg.com/736x/9d/9f/d3/9d9fd33f894700f6dc85acb005ce2ea3.jpg",
         "cara_memasak": [
             "Kupas apel, potong dadu, masak dengan brown sugar hingga lembut",
             "Campur tepung terigu, baking powder, gula halus, dan margarin hingga berbutir",
             "Tambahkan telur kuning dan air dingin, uleni hingga kalis",
             "Diamkan adonan dalam kulkas 15 menit",
             "Gilas adonan, letakkan di loyang pie",
             "Isi dengan apel yang sudah dimasak",
             "Tutup dengan adonan sisa, beri lubang kecil, panggang 180°C selama 25-30 menit"
         ]},
        {"nama": "Custrad🍮", "waktu": 10, "bahan": ["40g kis custrad tepung", "500 ml susu cair", "1 telur kuning", "100g gula halus",
                                                     "1 sdm vanilli", "3 sdm air dingin"], "rating": 4,
         "gambar_url": "https://i.pinimg.com/1200x/c3/57/1c/c3571cbd190d7fc9694a3b7382909d87.jpg",
         "cara_memasak": [
             "Larutkan tepung custard dengan air dingin hingga rata",
             "Panaskan susu cair dan gula hingga mendidih",
             "Masukkan larutan custard ke susu panas sambil diaduk terus",
             "Tambahkan telur kuning dan vanili, aduk cepat",
             "Masak dengan api kecil sambil terus diaduk hingga mengental",
             "Tuang ke cetakan dan dinginkan dalam kulkas minimal 2 jam",
             "Sajikan dingin"
         ]},
        {"nama": "Pretzel🥨", "waktu": 20, "bahan": ["350g tepung terigu tinggi protein", "250 ml susu cair", "60g brown sugar", "15g gula halus",
                                                     "1 sdm vanilli", "3 sdm minyak", "4 sdm ragi", "3 sdm garam"], "rating": 4,
         "gambar_url": "https://i.pinimg.com/736x/1a/a0/1f/1aa01f7a83f9a85de57d4990147a5016.jpg",
         "cara_memasak": [
             "Larutkan ragi dalam susu hangat dengan sedikit gula, diamkan 5 menit",
             "Campurkan tepung, brown sugar, gula halus, vanili, dan minyak",
             "Tuang larutan ragi ke campuran tepung, uleni hingga kalis",
             "Diamkan 30 menit hingga mengembang",
             "Bentuk adonan seperti tali, lalu bentuk pretzel",
             "Rebus air dengan garam, celupkan pretzel 30 detik tiap sisi",
             "Panggang dalam oven 200°C selama 12-15 menit hingga kecoklatan"
         ]},
    ]

def tambah_resep(nama, waktu, bahan, gambar_url="", cara_memasak=[]):
    st.session_state.resep.append({
        "nama": nama,
        "waktu": waktu,
        "bahan": bahan,
        "rating": 5,
        "gambar_url": gambar_url if gambar_url else "https://images.unsplash.com/photo-1495147466023-ac5c588e2e94?w=600",
        "cara_memasak": cara_memasak if cara_memasak else ["Belum ada instruksi memasak"]
    })

st.title("📘🍰 Buku Resep Kue")

menu = st.sidebar.radio("Menu Utama", ["Lihat Resep", "Tambah Resep", "Cari Resep", "Statistik"])

if menu == "Lihat Resep":
    st.header("📋 Daftar Resep")

    for i, r in enumerate(st.session_state.resep, start=1):
        with st.expander(f"{i}. {r['nama']} (Rating {r['rating']}/5)"):

            if "gambar_url" in r and r["gambar_url"]:
                st.image(r["gambar_url"], width=400, caption=r["nama"])
            
            st.write(f"⏱ Waktu: **{r['waktu']} menit**")
            st.write("📌 Bahan:")
            for b in r["bahan"]:
                st.write(f"- {b}")

            if "cara_memasak" in r and r["cara_memasak"]:
                st.write("👩‍🍳 Cara Memasak:")
                for idx, langkah in enumerate(r["cara_memasak"], start=1):
                    st.write(f"{idx}. {langkah}")

elif menu == "Tambah Resep":
    st.header("➕ Tambah Resep Baru")

    nama = st.text_input("Nama kue")
    waktu = st.number_input("Waktu memasak (menit)", min_value=1)

    st.write("Bahan (pisahkan dengan koma):")
    bahan_input = st.text_input("contoh: gula, tepung, telur")
    
    gambar_url = st.text_input("URL Gambar (opsional)", placeholder="https://example.com/image.jpg")
    
    st.write("Cara Memasak (pisahkan tiap langkah dengan enter):")
    cara_memasak_input = st.text_area("contoh:\nCampurkan bahan A dan B\nAduk hingga rata\nPanggang 30 menit")

    if st.button("Simpan Resep"):
        if nama and bahan_input:
            bahan_list = [b.strip() for b in bahan_input.split(",")]
            cara_memasak_list = [c.strip() for c in cara_memasak_input.split("\n") if c.strip()]
            tambah_resep(nama, waktu, bahan_list, gambar_url, cara_memasak_list)
            st.success("Resep berhasil ditambahkan!")
        else:
            st.error("Nama dan bahan wajib diisi.")

elif menu == "Cari Resep":
    st.header("🔍 Cari Resep")

    keyword = st.text_input("Masukkan nama kue")

    if keyword:
        hasil = [r for r in st.session_state.resep if keyword.lower() in r["nama"].lower()]

        if hasil:
            st.write(f"Ditemukan {len(hasil)} hasil:")
            for r in hasil:
                with st.expander(r["nama"]):
                    if "gambar_url" in r and r["gambar_url"]:
                        st.image(r["gambar_url"], width=400, caption=r["nama"])
                    
                    st.write(f"⏱ Waktu: {r['waktu']} menit")
                    st.write("🧺 Bahan:")
                    for b in r["bahan"]:
                        st.write(f"- {b}")
                    if "cara_memasak" in r and r["cara_memasak"]:
                        st.write("👩‍🍳 Cara Memasak:")
                        for idx, langkah in enumerate(r["cara_memasak"], start=1):
                            st.write(f"{idx}. {langkah}")
        else:
            st.warning("Resep tidak ditemukan")

elif menu == "Statistik":
    st.header("📊 Statistik Resep")

    total = len(st.session_state.resep)
    mudah = sum(1 for r in st.session_state.resep if r["waktu"] <= 45)
    sedang = total - mudah

    st.metric("Total Resep", total)
    st.metric("Resep Cepat (≤45 menit)", mudah)
    st.metric("Resep Sedang/Lama", sedang)

    st.write("---")
    persen_mudah = (mudah / total * 100) if total > 0 else 0
    st.write(f"Persentase resep cepat: **{persen_mudah:.1f}%**")