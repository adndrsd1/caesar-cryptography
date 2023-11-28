import string
import streamlit as st

abjad = string.ascii_letters

def enkripsi(pesan, key):
    cipher = ''
    for i in pesan:
        if i in abjad:
            k = abjad.find(i)
            k = (k + key) % 100
            cipher = cipher + abjad[k]
        else:
            cipher = cipher + i
    return cipher

def dekripsi(cipher, key):
    pesan = ''
    for i in cipher:
        if i in abjad:
            k = abjad.find(i)
            k = (k - key) % 100
            pesan = pesan + abjad[k]
        else:
            pesan = pesan + i
    return pesan

if __name__ == '__main__':
    st.set_page_config("Cryptography - Kelompok 3", page_icon="🔒", layout="wide")
    st.title("🔐CAESAR CIPHER🔐")
    with st.expander("What's Caesar Cipher?"):
        st.markdown("""
                    Caesar Cipher adalah salah satu teknik enkripsi tertua yang dikenal. 
                    Teknik ini merupakan teknik enkripsi yang paling sederhana dan paling banyak digunakan. 
                    Teknik ini menggunakan metode substitusi, yaitu menggantikan setiap huruf pada plaintext dengan huruf yang lain berdasarkan pada kunci yang ditentukan. 
                    Kunci pada Caesar Cipher adalah jumlah pergeseran yang dilakukan pada setiap huruf pada plaintext.
                    """)
        
    landing_page, encrypt_decrypt, about_us = st.tabs(["Landing Page", "Encrypt & Decrypt", "About Us"])

    with landing_page:
        st.title("🏠Home🏠")
        st.write("Selamat datang di aplikasi kami. Aplikasi ini digunakan untuk enkripsi dan deksripsi pesan dengan menggunakan algoritma caesar cipher.")

    with encrypt_decrypt:
        st.title("🔑Encrypt & Decrypt🔑")
        st.header("Encrypt & Decrypt")
        
        select = st.selectbox("Pilih menu :", ("Select", "Encrypt", "Decrypt"))
        if select == "Encrypt":
            st.subheader("Encrypt")
            pesan = st.text_area("Masukkan pesan :")
            key_encrypt = st.number_input("Masukkan kunci untuk enkripsi : ", value=0,  key="key_encrypt")
            st.write("Key: ", key_encrypt)
            show_hide_checkbox = st.checkbox("Show/Hide Chiper text")
            if show_hide_checkbox:
                st.write("Chiper text :")
                st.code("{}".format(enkripsi(pesan, key_encrypt)))
            else:
                st.code("{}".format("*" * len(enkripsi(pesan, key_encrypt))))

        elif select == "Decrypt":
            st.subheader("Decrypt")
            cipher = st.text_area("Masukkan cipher text :")
            key_decrypt = st.number_input("Masukkan kunci untuk dekripsi : ", value=0, key="key_decrypt")
            st.write("Key: ", key_decrypt)
            show_hide_checkbox = st.checkbox("Show/Hide Message text")
            if show_hide_checkbox:
                st.write("Message text :")
                st.code("{}".format(dekripsi(cipher, key_decrypt)))
            else:
                st.code("{}".format("*" * len(dekripsi(cipher, key_decrypt))))

        else:
            st.write("Silakan pilih menu")

    with about_us:
        st.header("About Us")
        
        st.markdown('''
                    ##### Kelompok 3:
                    - 2210511050 - Adrian Fakhriza Hakim
                    - 2210511056 - Adinda Rizki Sya'bana Diva
                    - 2210511062 - Aditya Ega Pratama
                    - 2210511072 - Edwina Martha Putri
                    - 2210511083 - Muh. Alif Alfattah Riu
                    ''')
        st.write("Copyright ©️ 2023 Kelompok 3")
