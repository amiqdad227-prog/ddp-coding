import streamlit as st

st.title("Form Data Diri")
st.write("Silahkan isi data diri anda")
st.write("Made by miqdad")

with st.form("form_data_diri"):
    nama = st.text_input("Nama")
    alamat = st.text_input("Alamat")
    usia = st.text_input("usia")
    submit = st.form_submit_button("Submit")

if submit:
    st.success(f"terima kasih {nama} telah mengisi form data diri")
    st.write(f"Nama : {nama}")
    st.write(f"Alamat : {alamat}")
    st.write(f"Usia : {usia}")
