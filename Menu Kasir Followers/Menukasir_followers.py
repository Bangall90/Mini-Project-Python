import streamlit as st

st.title("💰 Top Up Followers")

tiktok_followers = {
    "100 tt": 5000,
    "500 tt": 15000,
    "1000 tt": 25000,
    "5000 tt": 100000
}

instagram_followers = {
    "100 ig": 10000,
    "500 ig": 50000,
    "1000 ig": 100000,
    "5000 ig": 500000
}

facebook_followers = {
    "100 fb": 5000,
    "500 fb": 25000,
    "1000 fb": 50000,
    "5000 fb": 250000
}

semua_produk = {**tiktok_followers, **instagram_followers, **facebook_followers}

if "keranjang" not in st.session_state:
    st.session_state.keranjang = []

st.subheader("📋 Pricelist")

st.write("### TikTok Followers")
for nama, harga in tiktok_followers.items():
    st.write(f"{nama} = Rp{harga}")

st.write("### Instagram Followers")
for nama, harga in instagram_followers.items():
    st.write(f"{nama} = Rp{harga}")

st.write("### Facebook Followers")
for nama, harga in facebook_followers.items():
    st.write(f"{nama} = Rp{harga}")

st.subheader("🛒 Pilih Produk")

produk = st.selectbox("Pilih produk:", list(semua_produk.keys()))

if st.button("Tambah ke Keranjang"):
    st.session_state.keranjang.append(produk)
    st.success(f"{produk} ditambahkan!")

st.subheader("🧾 Keranjang")

total = 0

if st.session_state.keranjang:
    for item in st.session_state.keranjang:
        harga = semua_produk[item]
        st.write(f"{item} = Rp{harga}")
        total += harga

    st.write("### Total = Rp", total)
else:
    st.write("Keranjang kosong")

# Tombol reset
if st.button("Reset Keranjang"):
    st.session_state.keranjang = []
    st.warning("Keranjang dikosongkan")