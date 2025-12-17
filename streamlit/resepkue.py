import streamlit as st

if "resep" not in st.session_state:
    st.session_state.resep = [
        {"nama": "Brownies🍪", "waktu": 45, "bahan": ["100g mentega","200g dark coklat", "2 telur", "150g gula putih",
                                                       "100g tepung terigu", "1 sdt garam", "40g cocoa powder"], "rating": 5},
        {"nama": "Nastar🍍", "waktu": 60, "bahan": ["270g tepung terigu", "50g gula halus", "1 telur", "26g susu bubuk",
                                                     "30g tepung maizena", "200g mentega", "7g selai nanas"], "rating": 4},
        {"nama": "Donat🍩", "waktu": 30, "bahan": ["20 sdm tepung terigu tinggi protein", "3 sdm gula", "1 telur", "2 sdm susu bubuk",
                                                     "3g ragi", "130ml susu cair", "7g selai strawberry", "2 sdm baking powder"], "rating": 4.5},
        {"nama": "Waffle🧇", "waktu": 10, "bahan": ["7 sdm tepung terigu rendah protein", "1 sdm baking powder", "1 telur kuning", "1 sdm susu bubuk",
                                                     "100ml susu cair", "2 sdm minyak", "5 sdm saus caramel", "2 buah strawberry"], "rating": 5},
        {"nama": "Apple Pie🥧", "waktu": 25, "bahan": ["133g tepung terigu", "1,5 sdm baking powder", "1 telur kuning", "15g gula halus",
                                                     "75g margarin", "1 sdm air dingin", "3 buah apel", "1 sdm brown sugar"], "rating": 5},
        {"nama": "Custrad🍮", "waktu": 10, "bahan": ["40g kis custrad tepung", "500 ml susu cair", "1 telur kuning", "100g gula halus",
                                                     "1 sdm vanilli", "3 sdm air dingin"], "rating": 4},
        {"nama": "Pretzel🥨", "waktu": 20, "bahan": ["350g tepung terigu tinggi protein", "250 ml susu cair", "60g brown sugar", "15g gula halus",
                                                     "1 sdm vanilli", "3 sdm minyak", "4 sdm ragi", "3 sdm garam"], "rating": 4},
    ]

def tambah_resep(nama, waktu, bahan):
    st.session_state.resep.append({
        "nama": nama,
        "waktu": waktu,
        "bahan": bahan,
        "rating": 5,
    })

st.title("📘🍰 Buku Resep Kue")

menu = st.sidebar.radio("Menu Utama", ["Lihat Resep", "Tambah Resep", "Cari Resep", "Statistik"])

if menu == "Lihat Resep":
    st.header("📋 Daftar Resep")

    for i, r in enumerate(st.session_state.resep, start=1):
        with st.expander(f"{i}. {r['nama']} (Rating {r['rating']}/5)"):
            st.write(f"⏱ Waktu: **{r['waktu']} menit**")
            st.write("📌 Bahan:")
            for b in r["bahan"]:
                st.write(f"- {b}")

elif menu == "Tambah Resep":
    st.header("➕ Tambah Resep Baru")

    nama = st.text_input("Nama kue")
    waktu = st.number_input("Waktu memasak (menit)", min_value=1)

    st.write("Bahan (pisahkan dengan koma):")
    bahan_input = st.text_input("contoh: gula, tepung, telur")

    if st.button("Simpan Resep"):
        if nama and bahan_input:
            bahan_list = [b.strip() for b in bahan_input.split(",")]
            tambah_resep(nama, waktu, bahan_list)
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
                    st.write(f"⏱ Waktu: {r['waktu']} menit")
                    st.write("🧺 Bahan:")
                    for b in r["bahan"]:
                        st.write(f"- {b}")
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