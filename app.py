import streamlit as st
import sys
sys.path.insert(0, '.')

from ciphers import (
    VigenereCipher, 
    AffineCipher, 
    PlayfairCipher, 
    HillCipher, 
    EnigmaCipher
)

# Konfigurasi halaman
st.set_page_config(
    page_title="Kriptografi Klasik",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inisialisasi session state
if 'copied' not in st.session_state:
    st.session_state.copied = False
if 'last_result' not in st.session_state:
    st.session_state.last_result = None

# Custom CSS untuk interaktivitas yang lebih baik
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        padding: 20px;
        background: linear-gradient(135deg, #FFFFFF 0%, rgba(144, 238, 144, 0.08) 100%);
        min-height: 100vh;
    }
    
    .stApp {
        background: linear-gradient(135deg, #FFFFFF 0%, rgba(144, 238, 144, 0.08) 100%);
    }
    
    .sidebar .sidebar-content {
        background-color: rgba(51, 51, 51, 0.95);
    }
    
    .cipher-box {
        background-color: rgba(240, 242, 246, 0.95);
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .cipher-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
    }
    
    .result-box {
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
        border-left: 5px solid #4caf50;
        box-shadow: 0 4px 12px rgba(76, 175, 80, 0.15);
    }
    
    .error-box {
        background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
        border-left: 5px solid #f44336;
        box-shadow: 0 4px 12px rgba(244, 67, 54, 0.15);
    }
    
    .title-section {
        text-align: center;
        color: white;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    .info-section {
        background-color: rgba(33, 150, 243, 0.15);
        border-left: 4px solid #2196f3;
        padding: 15px;
        border-radius: 8px;
        margin: 15px 0;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(76, 175, 80, 0.4);
    }
    
    .stTab {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar untuk navigasi dengan menu yang lebih interaktif
with st.sidebar:
    col1, col2 = st.columns([4, 1])
    with col1:
        st.title("🔐 Kriptografi Klasik")
    
    st.markdown("---")
    
    # Info box di sidebar
    with st.expander("ℹ️ Tentang Aplikasi", expanded=False):
        st.markdown("""
        **Aplikasi Kriptografi Klasik**
        
        Aplikasi interaktif untuk:
        - ✅ Enkripsi & Dekripsi
        - 🔧 Berbagai algoritma
        - 📊 Visualisasi proses
        - 🎨 Interface yang ramah pengguna
        """)
    
    st.markdown("---")


    cipher_choice = st.sidebar.radio(
        "🔒 Pilih Algoritma Cipher:",
        ["Vigenere Cipher", "Affine Cipher", "Playfair Cipher", "Hill Cipher", "Enigma Cipher"],
        index=0
    )
    
    st.markdown("---")
    
    # Menu tambahan di sidebar
    with st.expander("⚙️ Pengaturan", expanded=False):
        st.write("**Pilihan Tampilan:**")
        show_matrix = st.checkbox("Tampilkan Detail Matriks", value=True)
        use_tabs = st.checkbox("Gunakan Tabs untuk Input/Output", value=True)
    
    st.markdown("---")
    st.info("💡 Pro Tip: Sidebar ini bisa dibuka tutup dengan klik tombol panah di atas!")
    
    # Footer sidebar
    st.markdown("""
    <div style='text-align: center; font-size: 11px; color: gray; margin-top: 20px;'>
    Made with ❤️ using Streamlit
    </div>
    """, unsafe_allow_html=True)

# ==================== VIGENERE CIPHER ====================
if cipher_choice == "Vigenere Cipher":
    st.title("🔐 Vigenere Cipher")
    
    st.markdown("""
    **Vigenere Cipher** adalah algoritma enkripsi simetris yang menggunakan kunci berulang untuk 
    mengenkripsi plaintext. Setiap huruf plaintext digeser oleh jumlah yang ditentukan oleh huruf 
    yang sesuai dalam kunci.
    """)
    
    # Inisialisasi session state
    if 'vigenere_result' not in st.session_state:
        st.session_state.vigenere_result = None
    if 'vigenere_result_type' not in st.session_state:
        st.session_state.vigenere_result_type = None
    
    # Gunakan tabs untuk membuat interface lebih interaktif
    tab1, tab2 = st.tabs(["📝 Input", "📊 Output"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Pilihan Mode")
            mode = st.radio("Pilih Mode:", ["🔒 Enkripsi", "🔓 Dekripsi"], key="vigenere_mode")
        
        with col2:
            st.subheader("Konfigurasi")
            key = st.text_input("Masukkan Kunci:", type="password", placeholder="Kunci enkripsi/dekripsi")
        
        st.markdown("---")
        
        if mode == "🔒 Enkripsi":
            plaintext = st.text_area(
                "📄 Plaintext (Teks Asli):", 
                placeholder="Masukkan teks yang ingin dienkripsi...",
                height=150
            )
            
            if st.button("🔒 Enkripsi Sekarang", use_container_width=True, key="vigenere_encrypt"):
                if plaintext and key:
                    try:
                        ciphertext = VigenereCipher.encrypt(plaintext, key)
                        st.session_state.vigenere_result = ciphertext
                        st.session_state.vigenere_result_type = "encrypt"
                        st.success("✅ Enkripsi berhasil!")
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                else:
                    st.warning("⚠️ Masukkan plaintext dan kunci terlebih dahulu!")
        
        else:  # Dekripsi
            ciphertext = st.text_area(
                "📄 Ciphertext (Teks Terenkripsi):", 
                placeholder="Masukkan teks yang ingin didekripsi...",
                height=150
            )
            
            if st.button("🔓 Dekripsi Sekarang", use_container_width=True, key="vigenere_decrypt"):
                if ciphertext and key:
                    try:
                        plaintext = VigenereCipher.decrypt(ciphertext, key)
                        st.session_state.vigenere_result = plaintext
                        st.session_state.vigenere_result_type = "decrypt"
                        st.success("✅ Dekripsi berhasil!")
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                else:
                    st.warning("⚠️ Masukkan ciphertext dan kunci terlebih dahulu!")
    
    with tab2:
        if st.session_state.vigenere_result:
            if st.session_state.vigenere_result_type == "encrypt":
                st.subheader("🎯 Hasil Enkripsi")
            else:
                st.subheader("🎯 Hasil Dekripsi")
            
            st.code(st.session_state.vigenere_result, language="text")
            st.write("**Hasil:**", st.session_state.vigenere_result)
            
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Panjang teks:** {len(st.session_state.vigenere_result)} karakter")
            with col2:
                st.write(f"**Tipe:** {'Enkripsi' if st.session_state.vigenere_result_type == 'encrypt' else 'Dekripsi'}")
        else:
            st.info("💡 Lakukan enkripsi atau dekripsi untuk melihat hasil di sini")


# ==================== AFFINE CIPHER ====================
elif cipher_choice == "Affine Cipher":
    st.title("🔐 Affine Cipher")
    
    st.markdown("""
    **Affine Cipher** adalah algoritma enkripsi simetris yang menggunakan fungsi afin linear 
    untuk transformasi. Rumus: E(x) = (ax + b) mod 26, dimana a dan 26 harus coprime.
    """)
    
    # Inisialisasi session state
    if 'affine_result' not in st.session_state:
        st.session_state.affine_result = None
    if 'affine_params' not in st.session_state:
        st.session_state.affine_params = {}
    
    tab1, tab2 = st.tabs(["⚙️ Konfigurasi", "📊 Output"])
    
    with tab1:
        st.info("⚠️ **Catatan Penting:** Nilai a harus coprime dengan 26. Nilai a yang valid: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            a = st.number_input("Nilai a (multiplier):", min_value=1, max_value=25, value=5)
        
        with col2:
            b = st.number_input("Nilai b (shift):", min_value=0, max_value=25, value=8)
        
        with col3:
            mode = st.radio("Mode:", ["🔒 Enkripsi", "🔓 Dekripsi"], key="affine_mode")
        
        st.markdown("---")
        
        if mode == "🔒 Enkripsi":
            plaintext = st.text_area(
                "📄 Plaintext:", 
                placeholder="Masukkan teks yang akan dienkripsi",
                height=150
            )
            
            if st.button("🔒 Enkripsi Sekarang", use_container_width=True, key="affine_encrypt"):
                if plaintext:
                    try:
                        ciphertext = AffineCipher.encrypt(plaintext, int(a), int(b))
                        st.session_state.affine_result = ciphertext
                        st.session_state.affine_params = {"a": a, "b": b, "type": "encrypt"}
                        st.success("✅ Enkripsi berhasil!")
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                else:
                    st.warning("⚠️ Masukkan plaintext terlebih dahulu!")
        
        else:  # Dekripsi
            ciphertext = st.text_area(
                "📄 Ciphertext:", 
                placeholder="Masukkan teks yang akan didekripsi",
                height=150
            )
            
            if st.button("🔓 Dekripsi Sekarang", use_container_width=True, key="affine_decrypt"):
                if ciphertext:
                    try:
                        plaintext = AffineCipher.decrypt(ciphertext, int(a), int(b))
                        st.session_state.affine_result = plaintext
                        st.session_state.affine_params = {"a": a, "b": b, "type": "decrypt"}
                        st.success("✅ Dekripsi berhasil!")
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                else:
                    st.warning("⚠️ Masukkan ciphertext terlebih dahulu!")
    
    with tab2:
        if st.session_state.affine_result:
            if st.session_state.affine_params.get("type") == "encrypt":
                st.subheader("📊 Hasil Enkripsi")
            else:
                st.subheader("📊 Hasil Dekripsi")
            
            st.code(st.session_state.affine_result, language="text")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Parameter a", st.session_state.affine_params.get("a", ""))
            with col2:
                st.metric("Parameter b", st.session_state.affine_params.get("b", ""))
            
            st.write("**Hasil:**", st.session_state.affine_result)
        else:
            st.info("💡 Lakukan enkripsi atau dekripsi untuk melihat hasil di sini")


# ==================== PLAYFAIR CIPHER ====================
elif cipher_choice == "Playfair Cipher":
    st.title("🔐 Playfair Cipher")
    
    st.markdown("""
    **Playfair Cipher** adalah algoritma enkripsi simetris yang menggunakan matriks 5x5 
    yang berisi huruf-huruf alfabet (I dan J dianggap sebagai satu huruf). Enkripsi dilakukan 
    pada pasangan huruf (digraph) bukan huruf individual.
    """)
    
    # Inisialisasi session state
    if 'playfair_result' not in st.session_state:
        st.session_state.playfair_result = None
    if 'playfair_type' not in st.session_state:
        st.session_state.playfair_type = None
    
    tab1, tab2, tab3 = st.tabs(["🔑 Kunci", "📝 Proses", "📊 Output"])
    
    with tab1:
        st.subheader("Masukkan Kunci Playfair")
        key = st.text_input("🔑 Kunci:", placeholder="Masukkan kunci enkripsi/dekripsi", key="playfair_key")
        
        if key:
            st.success(f"✅ Kunci diterima: {key}")
            
            with st.expander("📊 Tampilkan Matriks Playfair", expanded=True):
                matrix = PlayfairCipher.create_matrix(key)
                matrix_display = "\n".join([" ".join(row) for row in matrix])
                st.code(matrix_display, language="text")
                
                # Tampilkan matriks dengan grid
                col_grid = st.columns(5)
                for i, row in enumerate(matrix):
                    for j, char in enumerate(row):
                        with col_grid[j]:
                            st.markdown(f"""
                            <div style='background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%); 
                            color: white; padding: 10px; text-align: center; border-radius: 5px; font-weight: bold;'>
                            {char}
                            </div>
                            """, unsafe_allow_html=True)
        else:
            st.warning("⚠️ Masukkan kunci untuk melihat matriks")
    
    with tab2:
        mode = st.radio("Pilih Mode:", ["🔒 Enkripsi", "🔓 Dekripsi"], key="playfair_mode")
        
        if mode == "🔒 Enkripsi":
            plaintext = st.text_area(
                "📄 Plaintext:", 
                placeholder="Masukkan teks yang akan dienkripsi",
                height=150
            )
            
            if st.button("🔒 Enkripsi Sekarang", use_container_width=True, key="playfair_encrypt"):
                if plaintext and key:
                    try:
                        ciphertext = PlayfairCipher.encrypt(plaintext, key)
                        st.session_state.playfair_result = ciphertext
                        st.session_state.playfair_type = "encrypt"
                        st.success("✅ Enkripsi berhasil!")
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                else:
                    st.warning("⚠️ Masukkan plaintext dan kunci terlebih dahulu!")
        
        else:  # Dekripsi
            ciphertext = st.text_area(
                "📄 Ciphertext:", 
                placeholder="Masukkan teks yang akan didekripsi",
                height=150
            )
            
            if st.button("🔓 Dekripsi Sekarang", use_container_width=True, key="playfair_decrypt"):
                if ciphertext and key:
                    try:
                        plaintext = PlayfairCipher.decrypt(ciphertext, key)
                        st.session_state.playfair_result = plaintext
                        st.session_state.playfair_type = "decrypt"
                        st.success("✅ Dekripsi berhasil!")
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                else:
                    st.warning("⚠️ Masukkan ciphertext dan kunci terlebih dahulu!")
    
    with tab3:
        if st.session_state.playfair_result:
            if st.session_state.playfair_type == "encrypt":
                st.subheader("📊 Hasil Enkripsi")
            else:
                st.subheader("📊 Hasil Dekripsi")
            
            st.code(st.session_state.playfair_result, language="text")
            st.write("**Hasil:**", st.session_state.playfair_result)
            st.write(f"**Panjang:** {len(st.session_state.playfair_result)} karakter")
        else:
            st.info("💡 Lakukan enkripsi atau dekripsi untuk melihat hasil di sini")


# ==================== HILL CIPHER ====================
elif cipher_choice == "Hill Cipher":
    st.title("🔐 Hill Cipher")
    
    st.markdown("""
    **Hill Cipher** adalah algoritma enkripsi simetris yang menggunakan aljabar linear. 
    Plaintext dibagi menjadi blok dan setiap blok dienkripsi menggunakan perkalian matriks modulo 26.
    """)
    
    # Inisialisasi session state
    if 'hill_result' not in st.session_state:
        st.session_state.hill_result = None
    if 'hill_type' not in st.session_state:
        st.session_state.hill_type = None
    
    tab1, tab2, tab3 = st.tabs(["🔑 Kunci Matriks", "📝 Proses", "📊 Output"])
    
    with tab1:
        st.subheader("Masukkan Matriks Kunci 2x2")
        st.info("ℹ️ Matriks harus invertible modulo 26 (determinan tidak habis dibagi 26)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Baris 1:**")
            k11 = st.number_input("K[1,1]:", min_value=0, max_value=25, value=3, key="hill_k11")
            k21 = st.number_input("K[2,1]:", min_value=0, max_value=25, value=5, key="hill_k21")
        
        with col2:
            st.write("**Baris 2:**")
            k12 = st.number_input("K[1,2]:", min_value=0, max_value=25, value=4, key="hill_k12")
            k22 = st.number_input("K[2,2]:", min_value=0, max_value=25, value=7, key="hill_k22")
        
        # Tampilkan matriks
        st.write("**Matriks Kunci Anda:**")
        st.latex(f"\\begin{{bmatrix}} {int(k11)} & {int(k12)} \\\\ {int(k21)} & {int(k22)} \\end{{bmatrix}}")
        
        key_matrix = [[int(k11), int(k12)], [int(k21), int(k22)]]
    
    with tab2:
        mode = st.radio("Pilih Mode:", ["🔒 Enkripsi", "🔓 Dekripsi"], key="hill_mode")
        
        if mode == "🔒 Enkripsi":
            plaintext = st.text_area(
                "📄 Plaintext (harus genap karakternya):", 
                placeholder="Masukkan teks yang akan dienkripsi (minimalkan 2 karakter, preferably genap)",
                height=150
            )
            
            if st.button("🔒 Enkripsi Sekarang", use_container_width=True, key="hill_encrypt"):
                if plaintext:
                    try:
                        ciphertext = HillCipher.encrypt(plaintext, key_matrix)
                        st.session_state.hill_result = ciphertext
                        st.session_state.hill_type = "encrypt"
                        st.success("✅ Enkripsi berhasil!")
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                else:
                    st.warning("⚠️ Masukkan plaintext terlebih dahulu!")
        
        else:  # Dekripsi
            ciphertext = st.text_area(
                "📄 Ciphertext:", 
                placeholder="Masukkan teks yang akan didekripsi",
                height=150
            )
            
            if st.button("🔓 Dekripsi Sekarang", use_container_width=True, key="hill_decrypt"):
                if ciphertext:
                    try:
                        plaintext = HillCipher.decrypt(ciphertext, key_matrix)
                        st.session_state.hill_result = plaintext
                        st.session_state.hill_type = "decrypt"
                        st.success("✅ Dekripsi berhasil!")
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                else:
                    st.warning("⚠️ Masukkan ciphertext terlebih dahulu!")
    
    with tab3:
        if st.session_state.hill_result:
            if st.session_state.hill_type == "encrypt":
                st.subheader("📊 Hasil Enkripsi")
            else:
                st.subheader("📊 Hasil Dekripsi")
            
            st.code(st.session_state.hill_result, language="text")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Panjang Input", len(st.session_state.hill_result))
            with col2:
                st.metric("Tipe", "Enkripsi" if st.session_state.hill_type == "encrypt" else "Dekripsi")
            
            st.write("**Hasil:**", st.session_state.hill_result)
        else:
            st.info("💡 Lakukan enkripsi atau dekripsi untuk melihat hasil di sini")


# ==================== ENIGMA CIPHER ====================
else:  # Enigma Cipher
    st.title("🔐 Enigma Cipher")
    
    st.markdown("""
    **Enigma Cipher** adalah algoritma enkripsi yang menggunakan mekanisme rotor untuk 
    menciptakan substitusi yang kompleks dan berubah-ubah. Setiap penekanan tombol menyebabkan 
    rotor berputar, menghasilkan enkripsi yang berbeda untuk huruf yang sama.
    """)
    
    # Inisialisasi session state
    if 'enigma_result' not in st.session_state:
        st.session_state.enigma_result = None
    if 'enigma_config' not in st.session_state:
        st.session_state.enigma_config = {}
    
    tab1, tab2, tab3 = st.tabs(["⚙️ Konfigurasi Rotor", "📝 Proses", "📊 Output"])
    
    # Konfigurasi rotor standard
    default_rotors = {
        "Rotor I": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "Rotor II": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "Rotor III": "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    }
    
    default_reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    
    with tab1:
        st.subheader("Pilih Konfigurasi Rotor")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            rotor1_choice = st.selectbox("🔄 Rotor 1:", list(default_rotors.keys()), key="enigma_r1")
        
        with col2:
            rotor2_choice = st.selectbox("🔄 Rotor 2:", list(default_rotors.keys()), index=1, key="enigma_r2")
        
        with col3:
            rotor3_choice = st.selectbox("🔄 Rotor 3:", list(default_rotors.keys()), index=2, key="enigma_r3")
        
        rotor1 = default_rotors[rotor1_choice]
        rotor2 = default_rotors[rotor2_choice]
        rotor3 = default_rotors[rotor3_choice]
        
        st.markdown("---")
        
        with st.expander("📋 Lihat Detail Konfigurasi Rotor", expanded=False):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.write(f"**Rotor 1:**")
                st.code(rotor1, language="text")
            
            with col2:
                st.write(f"**Rotor 2:**")
                st.code(rotor2, language="text")
            
            with col3:
                st.write(f"**Rotor 3:**")
                st.code(rotor3, language="text")
            
            st.write(f"**Reflector:**")
            st.code(default_reflector, language="text")
    
    with tab2:
        mode = st.radio("Pilih Mode:", ["🔒 Enkripsi", "🔓 Dekripsi"], key="enigma_mode")
        
        if mode == "🔒 Enkripsi":
            plaintext = st.text_area(
                "📄 Plaintext:", 
                placeholder="Masukkan teks yang akan dienkripsi",
                height=150
            )
            
            if st.button("🔒 Enkripsi Sekarang", use_container_width=True, key="enigma_encrypt"):
                if plaintext:
                    try:
                        enigma = EnigmaCipher(rotor1, rotor2, rotor3, default_reflector)
                        ciphertext = enigma.encrypt(plaintext)
                        st.session_state.enigma_result = ciphertext
                        st.session_state.enigma_config = {
                            "type": "encrypt",
                            "r1": rotor1_choice,
                            "r2": rotor2_choice,
                            "r3": rotor3_choice
                        }
                        st.success("✅ Enkripsi berhasil!")
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                else:
                    st.warning("⚠️ Masukkan plaintext terlebih dahulu!")
        
        else:  # Dekripsi
            ciphertext = st.text_area(
                "📄 Ciphertext:", 
                placeholder="Masukkan teks yang akan didekripsi",
                height=150
            )
            
            if st.button("🔓 Dekripsi Sekarang", use_container_width=True, key="enigma_decrypt"):
                if ciphertext:
                    try:
                        enigma = EnigmaCipher(rotor1, rotor2, rotor3, default_reflector)
                        plaintext = enigma.decrypt(ciphertext)
                        st.session_state.enigma_result = plaintext
                        st.session_state.enigma_config = {
                            "type": "decrypt",
                            "r1": rotor1_choice,
                            "r2": rotor2_choice,
                            "r3": rotor3_choice
                        }
                        st.success("✅ Dekripsi berhasil!")
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                else:
                    st.warning("⚠️ Masukkan ciphertext terlebih dahulu!")
    
    with tab3:
        if st.session_state.enigma_result:
            if st.session_state.enigma_config.get("type") == "encrypt":
                st.subheader("📊 Hasil Enkripsi")
            else:
                st.subheader("📊 Hasil Dekripsi")
            
            st.code(st.session_state.enigma_result, language="text")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Panjang Output", len(st.session_state.enigma_result))
            with col2:
                st.metric("Tipe", "Enkripsi" if st.session_state.enigma_config.get("type") == "encrypt" else "Dekripsi")
            
            st.write("**Hasil:**", st.session_state.enigma_result)
            
            with st.expander("🔍 Informasi Konfigurasi yang Digunakan"):
                st.write(f"- Rotor 1: {st.session_state.enigma_config.get('r1', 'N/A')}")
                st.write(f"- Rotor 2: {st.session_state.enigma_config.get('r2', 'N/A')}")
                st.write(f"- Rotor 3: {st.session_state.enigma_config.get('r3', 'N/A')}")
        else:
            st.info("💡 Lakukan enkripsi atau dekripsi untuk melihat hasil di sini")


# Footer dengan styling yang lebih baik
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 30px 0;'>
    <h2 style='color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);'>
        🔐 Aplikasi Kriptografi Klasik
    </h2>
    <p style='color: rgba(255,255,255,0.8); font-size: 14px;'>
        Implementasi: Vigenere • Affine • Playfair • Hill • Enigma Cipher
    </p>
    <p style='color: rgba(255,255,255,0.6); font-size: 12px;'>
        Dibuat untuk Tugas Kriptografi Semester 6 | Made with ❤️ using Streamlit
    </p>
</div>
""", unsafe_allow_html=True)

# Session state untuk menampilkan tips
if 'show_tips' not in st.session_state:
    st.session_state.show_tips = False

with st.expander("💡 Tips Penggunaan"):
    st.markdown("""
    ### Panduan Penggunaan Aplikasi
    
    ✅ **Untuk Semua Cipher:**
    - Gunakan sidebar untuk memilih algoritma cipher
    - Sidebar bisa dibuka/ditutup dengan klik tombol panah (hamburger menu)
    - Setiap cipher memiliki tab terpisah untuk organisasi yang lebih baik
    
    📝 **Tips Input:**
    - Gunakan teks yang jelas dan mudah dimengerti
    - Untuk enkripsi, masukkan plaintext yang ingin disandikan
    - Untuk dekripsi, masukkan ciphertext yang ingin dibuka sandi
    
    🔐 **Keamanan Kunci:**
    - Simpan kunci dengan aman
    - Jangan bagikan kunci kepada orang yang tidak terpercaya
    - Kunci yang sama digunakan untuk enkripsi dan dekripsi
    
    📊 **Hasil:**
    - Output akan ditampilkan di tab "Output"
    - Anda bisa menyalin hasil dengan tombol yang tersedia
    """)

# Statistik penggunaan
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📊 Cipher Tersedia", 5, delta="aktif")

with col2:
    st.metric("🔐 Tipe Operasi", 2, delta="Enkripsi & Dekripsi")

with col3:
    st.metric("⚙️ Interface", "Modern & Responsive", delta="v1.0")
