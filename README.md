# 🔐 Aplikasi Kriptografi Klasik - Streamlit Web Based

Aplikasi web berbasis Streamlit untuk enkripsi dan dekripsi menggunakan 5 algoritma kriptografi klasik sesuai dengan tugas Universitas.

## 📋 Daftar Algoritma yang Diimplementasikan

1. **Vigenere Cipher** - Enkripsi substitusi polialfabetik menggunakan kunci berulang
2. **Affine Cipher** - Enkripsi linear menggunakan fungsi afin E(x) = (ax + b) mod 26
3. **Playfair Cipher** - Enkripsi digraph menggunakan matriks 5x5
4. **Hill Cipher** - Enkripsi blok menggunakan aljabar linear dan matriks
5. **Enigma Cipher** - Enkripsi mekanis menggunakan rotor yang berputar

## 🚀 Cara Menjalankan Aplikasi

### Prasyarat
- Python 3.7 atau lebih tinggi
- pip package manager

### Langkah 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Langkah 2: Jalankan Aplikasi
```bash
streamlit run app.py
```

atau jika streamlit tidak berada di PATH:
```bash
python -m streamlit run app.py
```

### Langkah 3: Akses Aplikasi
Aplikasi akan otomatis membuka browser dengan URL:
- **Local URL**: http://localhost:8501
- **Network URL**: http://[IP-Anda]:8501

## 📖 Panduan Penggunaan

### 1. Vigenere Cipher
**Deskripsi**: Algoritma enkripsi simetris yang menggunakan kunci berulang.

**Cara Penggunaan**:
- Pilih mode: Enkripsi atau Dekripsi
- Masukkan plaintext/ciphertext
- Masukkan kunci (hanya huruf akan diproses)
- Klik tombol untuk enkripsi/dekripsi

**Contoh**:
- Plaintext: "HELLO WORLD"
- Kunci: "KEY"
- Ciphertext: "RIJVS UYVJN"

---

### 2. Affine Cipher
**Deskripsi**: Algoritma enkripsi linear menggunakan rumus E(x) = (ax + b) mod 26.

**Parameter**:
- **a** (multiplier): harus coprime dengan 26 (valid: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25)
- **b** (shift): nilai dari 0-25

**Cara Penggunaan**:
- Pilih nilai a dan b
- Masukkan plaintext/ciphertext
- Klik tombol untuk enkripsi/dekripsi

**Contoh**:
- Plaintext: "HELLO"
- a = 5, b = 8
- Ciphertext: "RCLLA"

---

### 3. Playfair Cipher
**Deskripsi**: Algoritma enkripsi digraph yang menggunakan matriks 5x5.

**Cara Penggunaan**:
- Masukkan kunci
- Aplikasi akan menampilkan matriks Playfair yang dihasilkan
- Masukkan plaintext/ciphertext
- Klik tombol untuk enkripsi/dekripsi

**Catatan**:
- Huruf J akan diganti dengan I
- Plaintext akan dipasang-pasangkan menjadi digraph
- Jika plaintext memiliki panjang ganjil, akan ditambahkan padding 'X'

**Contoh**:
- Plaintext: "SECRET"
- Kunci: "MONARCHY"
- Ciphertext: "GBOXPDQ"

---

### 4. Hill Cipher
**Deskripsi**: Algoritma enkripsi blok menggunakan aljabar linear dan perkalian matriks.

**Parameter**:
- Matriks Kunci 2x2 (K[1,1], K[1,2], K[2,1], K[2,2])
- Determinan matriks harus coprime dengan 26

**Cara Penggunaan**:
- Input nilai-nilai matriks kunci 2x2
- Masukkan plaintext dengan panjang genap (akan ditambah padding jika ganjil)
- Klik tombol untuk enkripsi/dekripsi

**Contoh**:
- Plaintext: "HELP"
- Matriks: [[3, 4], [5, 7]]
- Ciphertext: "BGOH"

---

### 5. Enigma Cipher
**Deskripsi**: Algoritma enkripsi mekanis yang menggunakan rotor yang berputar.

**Komponen**:
- 3 buah Rotor dengan substitusi tetap
- 1 Reflector untuk jalur balik
- Plugboard untuk substitusi tambahan (opsional)

**Cara Penggunaan**:
- Pilih konfigurasi rotor (Rotor I, II, atau III untuk setiap posisi)
- Masukkan plaintext/ciphertext
- Klik tombol untuk enkripsi/dekripsi

**Catatan**:
- Enkripsi dan dekripsi menggunakan proses yang sama (simetris)
- Setiap penekanan tombol menyebabkan rotor berputar
- Rotor memiliki mekanisme double-stepping

**Contoh**:
- Plaintext: "HELLO"
- Rotor Configuration: I, II, III
- Ciphertext akan berubah tergantung posisi rotor

---

## 📁 Struktur File

```
kriptografi/
├── app.py                 # Aplikasi Streamlit utama
├── ciphers.py            # Implementasi semua algoritma cipher
├── requirements.txt      # Dependencies Python
├── README.md            # Dokumentasi ini
└── .streamlit/
    └── config.toml      # Konfigurasi Streamlit
```

## 🔧 Implementasi Detail

### File: `app.py`
Berisi:
- Interface Streamlit untuk semua cipher
- Navigasi sidebar untuk memilih algoritma
- Input form dan button untuk enkripsi/dekripsi
- Tampilan hasil dan error handling

### File: `ciphers.py`
Berisi implementasi class untuk:
- `VigenereCipher` - Vigenere Cipher
- `AffineCipher` - Affine Cipher dengan GCD dan modular inverse
- `PlayfairCipher` - Playfair dengan pembuatan matriks 5x5
- `HillCipher` - Hill Cipher dengan operasi matriks
- `EnigmaCipher` - Enigma dengan rotor dan reflector

## 📊 Fitur Tambahan

- ✅ Input validation dan error handling
- ✅ Tampilan matriks Playfair secara real-time
- ✅ Support untuk plaintext dengan spasi dan karakter khusus (hanya alfabet yang diproses)
- ✅ Interface yang user-friendly dengan sidebar navigation
- ✅ Penjelasan singkat untuk setiap algoritma

## ⚠️ Catatan Penting

1. **Keamanan**: Ini adalah implementasi cipher klasik untuk tujuan edukasi. Jangan digunakan untuk enkripsi data sensitif di dunia nyata.

2. **Karakter Input**: Hanya huruf A-Z yang diproses. Spasi dan karakter lain akan dihilangkan.

3. **Case Sensitivity**: Semua input akan dikonversi ke huruf besar (uppercase).

4. **Playfair Cipher**: Huruf J akan diganti dengan I secara otomatis.

## 🐛 Troubleshooting

**Error: "The term 'streamlit' is not recognized"**
- Solusi: Gunakan `python -m streamlit run app.py` atau install streamlit dengan `pip install streamlit`

**Error: "ModuleNotFoundError: No module named 'streamlit'"**
- Solusi: Jalankan `pip install -r requirements.txt`

**Port 8501 sudah digunakan**
- Solusi: Modifikasi file `.streamlit/config.toml` dan ubah nilai `port` ke port yang berbeda

## 📝 Contoh Lengkap

### Vigenere Cipher
```
Plaintext: ATTACKING AT DAWN
Kunci: LEMON
Ciphertext: LXFOPVEFRNHR
```

### Affine Cipher (a=5, b=8)
```
Plaintext: HELLO
Ciphertext: RCLLA
```

### Playfair Cipher
```
Plaintext: MEET ME AT THE USUAL PLACE AT TEN PM
Kunci: MONARCHY
Ciphertext: GBXFQYDGCWHCUAKGNVFQNYHDUQSKUIIGHH
```

### Hill Cipher
```
Plaintext: ACTHUSECON
Matriks: [[2,3], [5,7]]
Ciphertext: GTNHPSMEMP
```

### Enigma Cipher
```
Mode: Enkripsi
Plaintext: HELLO
Konfigurasi: Rotor I, II, III
Ciphertext: (tergantung posisi rotor awal)
```

## 👨‍💻 Author

Dibuat sebagai tugas Kriptografi Semester 6 - 2025/2026

## 📄 Lisensi

Untuk tujuan pendidikan

---

**Last Updated**: February 2026
