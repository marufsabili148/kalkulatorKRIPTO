# 🚀 SETUP DAN INSTALASI

Panduan lengkap untuk setup dan menjalankan aplikasi Kriptografi Klasik.

---

## ✅ Prasyarat

- **Python 3.7 atau lebih tinggi**
- **pip** (Python package manager)
- **Git** (optional, untuk clone repository)

### Verifikasi Instalasi Python

```powershell
# Windows PowerShell
python --version
pip --version
```

Jika belum install Python, download dari: https://www.python.org/downloads/

---

## 📥 Instalasi

### Step 1: Download/Clone Project

**Opsi A: Clone dari GitHub**
```powershell
git clone <your-github-url>
cd kriptografi
```

**Opsi B: Download Manual**
- Download semua file ke folder: `C:\...\kriptografi\`

### Step 2: Install Dependencies

```powershell
cd "C:\Users\MSI GF\Downloads\Akademik Kuliah\SMT 6\kriptografi"

# Install semua package yang diperlukan
pip install -r requirements.txt
```

**Package yang diinstall:**
- `streamlit` - Framework untuk web app
- `numpy` - Untuk operasi matriks (Hill Cipher)
- `pdfplumber` - Untuk membaca PDF
- `PyPDF2` - Untuk manipulasi PDF

---

## 🚀 Menjalankan Aplikasi

### Method 1: Menggunakan Streamlit Command (Recommended)

```powershell
cd "C:\Users\MSI GF\Downloads\Akademik Kuliah\SMT 6\kriptografi"
streamlit run app.py
```

### Method 2: Menggunakan Python Module

```powershell
cd "C:\Users\MSI GF\Downloads\Akademik Kuliah\SMT 6\kriptografi"
python -m streamlit run app.py
```

### Output yang Diharapkan:

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://[your-ip]:8501
```

---

## 🌐 Mengakses Aplikasi

### Local Access (Dari Komputer Sendiri)
- Buka Browser: `http://localhost:8501`
- URL: `http://127.0.0.1:8501`

### Network Access (Dari Komputer Lain)
- Ganti `localhost` dengan IP Address Anda
- Contoh: `http://192.168.1.100:8501`

### Untuk Mengetahui IP Address Anda

**Windows PowerShell:**
```powershell
ipconfig
# Cari IPv4 Address pada Ethernet atau WiFi adapter
```

**Command Prompt:**
```cmd
ipconfig
```

---

## 🧪 Testing Cipher Implementation

Untuk memverifikasi semua algoritma berfungsi dengan baik:

```powershell
cd "C:\Users\MSI GF\Downloads\Akademik Kuliah\SMT 6\kriptografi"
python test_ciphers.py
```

**Output yang Diharapkan:**
```
✅ VIGENERE CIPHER: PASS
✅ AFFINE CIPHER: PASS
✅ PLAYFAIR CIPHER: PASS
✅ HILL CIPHER: PASS
✅ ENIGMA CIPHER: PASS
Total: 5/5 tests passed
```

---

## 📁 Struktur File Project

```
kriptografi/
├── app.py                    # Aplikasi Streamlit utama
├── ciphers.py               # Implementasi semua algoritma
├── test_ciphers.py          # File testing
├── requirements.txt         # Dependencies
├── README.md                # Dokumentasi utama
├── SETUP.md                 # File ini
├── EXAMPLE_DATA.md          # Contoh penggunaan
└── .streamlit/
    └── config.toml          # Konfigurasi Streamlit
```

---

## 🔧 Konfigurasi Lanjutan

### Mengubah Port

Edit file `.streamlit/config.toml`:

```toml
[server]
port = 8502  # Ganti dengan port yang diinginkan
```

Lalu jalankan ulang aplikasi.

### Mengubah Theme

Edit file `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#F0F2F6"
secondaryBackgroundColor = "#E8F5E9"
textColor = "#31333F"
font = "sans serif"
```

---

## ❌ Troubleshooting

### 1. Error: "The term 'streamlit' is not recognized"

**Solusi:**
```powershell
# Gunakan python -m streamlit
python -m streamlit run app.py
```

Atau:
```powershell
# Reinstall streamlit
pip install --upgrade streamlit
```

---

### 2. Error: "ModuleNotFoundError: No module named 'streamlit'"

**Solusi:**
```powershell
# Install semua dependencies
pip install -r requirements.txt

# Atau install secara manual
pip install streamlit numpy pdfplumber PyPDF2
```

---

### 3. Error: "Port 8501 is already in use"

**Solusi Opsi A:** Kill proses yang menggunakan port
```powershell
# Windows PowerShell
Get-Process | Where-Object {$_.Handles -like "*8501*"} | Stop-Process
```

**Solusi Opsi B:** Gunakan port berbeda
```powershell
streamlit run app.py --server.port=8502
```

**Solusi Opsi C:** Edit config.toml
```toml
[server]
port = 8502
```

---

### 4. Error: "numpy.linalg.LinAlgError: Singular matrix"

**Konteks:** Error pada Hill Cipher

**Solusi:** Gunakan matriks yang determinannya coprime dengan 26.

Nilai determianan yang valid (coprime dengan 26):
```
1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25
```

**Test determinant:**
```python
import numpy as np

# Matriks Anda
K = [[3, 4], [5, 7]]
det = int(np.round(np.linalg.det(np.array(K)))) % 26
print(f"Determinant: {det}")
print(f"Valid: {det in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]}")
```

---

### 5. Aplikasi Lambat atau Tidak Responsif

**Solusi:**
```powershell
# Restart aplikasi
# 1. Tekan Ctrl+C di terminal
# 2. Run command baru:
python -m streamlit run app.py --client.showErrorDetails=true
```

---

### 6. Tidak Bisa Akses dari Komputer Lain

**Cek:**
1. Pastikan firewall tidak memblokir port 8501
2. Gunakan IP address lokal, bukan localhost
3. Pastikan kedua komputer dalam jaringan yang sama

**Edit config.toml:**
```toml
[server]
headless = true
port = 8501
address = "0.0.0.0"  # Aktifkan akses dari jaringan
```

---

## 📊 Verifikasi Instalasi

Jalankan script ini untuk memverifikasi setup:

```powershell
python -c "
import streamlit
import numpy
import pdfplumber
import PyPDF2
print('✅ Streamlit:', streamlit.__version__)
print('✅ NumPy:', numpy.__version__)
print('✅ pdfplumber: installed')
print('✅ PyPDF2: installed')
print('')
print('Setup berhasil! Jalankan: streamlit run app.py')
"
```

---

## 🔐 Untuk Development

### Struktur Code

**app.py** - Streamlit Interface
- Sidebar untuk navigasi
- 5 section untuk 5 cipher
- Input/output handling

**ciphers.py** - Implementasi Algoritma
- Class untuk setiap cipher
- Static methods untuk encrypt/decrypt
- Helper methods untuk pemrosesan teks

**test_ciphers.py** - Unit Testing
- Test setiap cipher
- Verifikasi enkripsi-dekripsi
- Summary report

---

## 📝 Best Practices

1. **Jangan modifikasi ciphers.py** kecuali untuk improvement
2. **Backup semua file** sebelum perubahan besar
3. **Commit ke git** setiap perubahan penting
4. **Testing** setelah perubahan code

---

## 📚 Dokumentasi Tambahan

- Baca `README.md` untuk panduan penggunaan lengkap
- Baca `EXAMPLE_DATA.md` untuk contoh enkripsi-dekripsi
- Lihat docstring di `ciphers.py` untuk detail implementasi

---

## 🎯 Checklist Sebelum Submit

- [ ] Setup berhasil tanpa error
- [ ] Aplikasi berjalan di `http://localhost:8501`
- [ ] Semua 5 cipher berfungsi (test pass)
- [ ] UI dapat diakses dan responsif
- [ ] Source code di GitHub atau Google Drive
- [ ] Documentation lengkap
- [ ] Contoh output ciphertext tersedia

---

## 📞 Support

Jika ada error, follow langkah-langkah:

1. **Baca error message** dengan teliti
2. **Cari di troubleshooting section** dokumentasi ini
3. **Check Python version:** `python --version`
4. **Reinstall packages:** `pip install -r requirements.txt --upgrade`
5. **Clear Streamlit cache:** `streamlit cache clear`

---

**Last Updated**: February 2026
**Status**: Ready for Production ✅
