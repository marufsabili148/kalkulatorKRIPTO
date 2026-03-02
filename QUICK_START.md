# 🚀 QUICK START GUIDE

Panduan cepat untuk menjalankan aplikasi dalam 2 menit.

---

## Step 1: Install Dependencies (1 menit)

Buka PowerShell dan jalankan:

```powershell
# Masuk ke folder project
cd "C:\Users\MSI GF\Downloads\Akademik Kuliah\SMT 6\kriptografi"

# Install semua dependencies
pip install -r requirements.txt
```

Tunggu hingga selesai. Output akan menunjukkan:
```
Successfully installed streamlit numpy pdfplumber PyPDF2
```

---

## Step 2: Jalankan Aplikasi (1 klik)

```powershell
# Jalankan aplikasi
streamlit run app.py
```

Jika error `streamlit not recognized`, gunakan:
```powershell
python -m streamlit run app.py
```

---

## Step 3: Akses di Browser

Aplikasi akan otomatis membuka di:
- **http://localhost:8501**

Atau buka manual di browser Anda.

---

## ✨ Selesai!

Aplikasi sudah siap digunakan. Anda bisa:

1. **Pilih Cipher** di sidebar (5 pilihan)
2. **Masukkan Teks** yang ingin dienkripsi/dekripsi
3. **Klik Tombol** untuk hasil
4. **Copy Output** untuk digunakan di tempat lain

---

## 📊 Test (Optional)

Untuk verifikasi semua cipher berfungsi:

```powershell
python test_ciphers.py
```

Output yang diharapkan:
```
✅ VIGENERE CIPHER: PASS
✅ AFFINE CIPHER: PASS
✅ PLAYFAIR CIPHER: PASS
✅ HILL CIPHER: PASS
✅ ENIGMA CIPHER: PASS
Total: 5/5 tests passed
```

---

## 🆘 Troubleshooting

### Masalah: Python tidak ditemukan
**Solusi:** Download dari https://www.python.org/downloads/

### Masalah: pip command tidak ditemukan  
**Solusi:** 
```powershell
python -m pip install -r requirements.txt
```

### Masalah: Streamlit command tidak ditemukan
**Solusi:**
```powershell
python -m streamlit run app.py
```

### Masalah: Port 8501 sudah digunakan
**Solusi:**
```powershell
streamlit run app.py --server.port=8502
```

---

## 📖 Dokumentasi Lengkap

- **README.md** - Panduan lengkap setiap cipher
- **SETUP.md** - Setup dan troubleshooting detail
- **EXAMPLE_DATA.md** - Contoh enkripsi untuk setiap cipher
- **PROJECT_SUMMARY.md** - Ringkasan project

---

## 💡 Tips

1. **Hanya huruf yang diproses** - Spasi dan karakter khusus akan dihindari
2. **Case insensitive** - Semua input akan menjadi huruf besar
3. **Copy-friendly** - Setiap output bisa langsung di-copy

---

**Status**: ✅ Ready to Use

Enjoy! 🎉
