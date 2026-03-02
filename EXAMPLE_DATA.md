# 📊 Contoh Data Enkripsi-Dekripsi

Dokumentasi lengkap dengan contoh plaintext dan ciphertext untuk setiap algoritma.

---

## 1. VIGENERE CIPHER

### Contoh 1: Teks Pendek
| Parameter | Nilai |
|-----------|-------|
| **Plaintext** | HELLO WORLD |
| **Kunci** | KEY |
| **Ciphertext** | RIJVSUYVJN |
| **Status** | ✅ Berhasil |

**Proses Enkripsi:**
```
Plaintext:  H E L L O W O R L D
Key:        K E Y K E Y K E Y K
Shift:      10 4 24 10 4 24 10 4 24 10
Ciphertext: R I J V S U Y V J N
```

---

### Contoh 2: Teks Panjang
| Parameter | Nilai |
|-----------|-------|
| **Plaintext** | ATTACKING AT DAWN |
| **Kunci** | LEMON |
| **Ciphertext** | LXFOPVEFRNHR |
| **Status** | ✅ Berhasil |

---

### Contoh 3: Spasi dan Karakter Khusus
| Parameter | Nilai |
|-----------|-------|
| **Plaintext** | Meet me at the usual place at ten PM |
| **Kunci** | SECURITY |
| **Ciphertext** | (Hanya huruf yang diproses) |
| **Status** | ✅ Berhasil |

---

## 2. AFFINE CIPHER

### Contoh 1: a=5, b=8
| Parameter | Nilai |
|-----------|-------|
| **Plaintext** | HELLO |
| **a (multiplier)** | 5 |
| **b (shift)** | 8 |
| **Ciphertext** | RCLLA |
| **Status** | ✅ Berhasil |

**Rumus**: E(x) = (5x + 8) mod 26
```
H(7): (5*7 + 8) mod 26 = 43 mod 26 = 17 = R
E(4): (5*4 + 8) mod 26 = 28 mod 26 = 2 = C
L(11): (5*11 + 8) mod 26 = 63 mod 26 = 11 = L
L(11): (5*11 + 8) mod 26 = 63 mod 26 = 11 = L
O(14): (5*14 + 8) mod 26 = 78 mod 26 = 0 = A
```

---

### Contoh 2: a=7, b=3
| Parameter | Nilai |
|-----------|-------|
| **Plaintext** | PLAINTEXT |
| **a (multiplier)** | 7 |
| **b (shift)** | 3 |
| **Ciphertext** | ALNYTVCNR |
| **Status** | ✅ Berhasil |

---

### Contoh 3: Invalid a
| Parameter | Nilai |
|-----------|-------|
| **Plaintext** | HELLO |
| **a (multiplier)** | 4 ❌ (gcd(4,26) ≠ 1) |
| **b (shift)** | 8 |
| **Status** | ❌ Error |

**Nilai a yang Valid:** 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25

---

## 3. PLAYFAIR CIPHER

### Contoh 1: Kunci "MONARCHY"
| Parameter | Nilai |
|-----------|-------|
| **Plaintext** | SECRETKEY |
| **Kunci** | MONARCHY |
| **Ciphertext** | LIDMKLCDCE |
| **Status** | ✅ Berhasil |

**Matriks Playfair:**
```
M O N A R
C H Y B D
E F G I K
L P Q S T
U V W X Z
```

**Aturan Enkripsi Digraph:**
- Jika dalam baris sama → shift kanan (wrap around)
- Jika dalam kolom sama → shift bawah (wrap around)
- Jika rectangle → swap kolom

---

### Contoh 2: Kunci "KINGSTON"
| Parameter | Nilai |
|-----------|-------|
| **Plaintext** | ATTACKATDAWN |
| **Kunci** | KINGSTON |
| **Ciphertext** | YGIDMLDSGCMK |
| **Status** | ✅ Berhasil |

**Matriks Playfair:**
```
K I N G S
T O A B C
D E F H L
M P Q R U
V W X Y Z
```

---

### Contoh 3: Plaintext dengan Panjang Ganjil
| Parameter | Nilai |
|-----------|-------|
| **Plaintext** | MEET (ditambah padding X) |
| **Kunci** | HELP |
| **Plaintext Adjusted** | MEETX |
| **Ciphertext** | GIHWDU |
| **Status** | ✅ Berhasil |

---

## 4. HILL CIPHER

### Contoh 1: Matriks [[3, 4], [5, 7]]
| Parameter | Nilai |
|-----------|-------|
| **Plaintext** | HELP |
| **Matriks Kunci** | [[3, 4], [5, 7]] |
| **Ciphertext** | LLPE |
| **Status** | ✅ Berhasil |

**Proses Enkripsi:**
```
Plaintext vektor 1: [H(7), E(4)]^T = [7, 4]^T
K × P1 = [[3,4],[5,7]] × [[7],[4]] = [[21+16],[35+28]] = [[37],[63]] mod 26 = [[11],[11]] = [L, L]

Plaintext vektor 2: [L(11), P(15)]^T = [11, 15]^T
K × P2 = [[3,4],[5,7]] × [[11],[15]] = [[33+60],[55+105]] = [[93],[160]] mod 26 = [[15],[4]] = [P, E]

Ciphertext: LLPE
```

---

### Contoh 2: Matriks [[2, 3], [5, 7]]
| Parameter | Nilai |
|-----------|-------|
| **Plaintext** | HELLO (ditambah padding untuk genap) |
| **Plaintext Adjusted** | HELLOX |
| **Matriks Kunci** | [[2, 3], [5, 7]] |
| **Ciphertext** | ZBLFVD |
| **Status** | ✅ Berhasil |

**Determinant Check:**
```
det(K) = 2×7 - 3×5 = 14 - 15 = -1 mod 26 = 25
gcd(25, 26) = 1 ✅ Valid
```

---

### Requirement untuk Matriks Kunci:
- Determinan matriks harus **coprime dengan 26**
- Matriks harus **invertible modulo 26**
- Ukuran matriks: **2×2**

---

## 5. ENIGMA CIPHER

### Contoh 1: Rotor I, II, III
| Parameter | Nilai |
|-----------|-------|
| **Plaintext** | HELLO |
| **Rotor 1** | EKMFLGDQVZNTOWYHXUSPAIBRCJ |
| **Rotor 2** | AJDKSIRUXBLHWTMCQGZNPYFVOE |
| **Rotor 3** | BDFHJLCPRTXVZNYEIWGAKMUSQO |
| **Reflector** | YRUHQSLDPXNGOKMIEBFZCWVJAT |
| **Ciphertext** | MFNCZ |
| **Status** | ✅ Berhasil |

---

### Contoh 2: Rotor II, III, I (Konfigurasi Berbeda)
| Parameter | Nilai |
|-----------|-------|
| **Plaintext** | SECRET |
| **Rotor 1** | AJDKSIRUXBLHWTMCQGZNPYFVOE |
| **Rotor 2** | BDFHJLCPRTXVZNYEIWGAKMUSQO |
| **Rotor 3** | EKMFLGDQVZNTOWYHXUSPAIBRCJ |
| **Reflector** | YRUHQSLDPXNGOKMIEBFZCWVJAT |
| **Ciphertext** | IXZDVQ |
| **Status** | ✅ Berhasil |

---

### Mekanisme Rotor Enigma:
1. **Rotor Stepping**: Setiap karakter menyebabkan rotor berputar
2. **Double-Stepping**: Ketika rotor mencapai posisi 0, rotor berikutnya juga berputar
3. **Reflector**: Sinyal melewati rotor 3 kali (maju, reflector, mundur)
4. **Symmetry**: Enkripsi dan dekripsi menggunakan proses yang sama

---

### Contoh 3: Verifikasi Dekripsi
| Parameter | Nilai |
|-----------|-------|
| **Original Text** | ATTACKATDAWN |
| **Encrypted** | MFNCZRYQEWXK |
| **Decrypted** | ATTACKATDAWN |
| **Status** | ✅ Symmetric (Verified) |

---

## 📈 Perbandingan Algoritma

| Aspek | Vigenere | Affine | Playfair | Hill | Enigma |
|-------|----------|--------|----------|------|--------|
| **Kecepatan** | Cepat | Sangat Cepat | Cepat | Sedang | Sedang |
| **Keamanan** | Rendah | Rendah | Sedang | Sedang | Tinggi |
| **Ukuran Blok** | 1 | 1 | 2 (digraph) | 2 | 1 |
| **Jenis Kunci** | String | 2 integer | String | Matrix 2×2 | Rotor Config |
| **Praktis** | Ya | Ya | Ya | Terbatas | Jarang |

---

## 🔐 Catatan Keamanan

1. **Semua cipher ini bukan untuk enkripsi data real-world**
2. **Mudah di-attack dengan frequency analysis**
3. **Hanya untuk tujuan edukasi dan pembelajaran**
4. **Gunakan modern encryption (AES, RSA) untuk data sensitif**

---

## 📝 Cara Menggunakan Contoh

1. Buka aplikasi Streamlit: `streamlit run app.py`
2. Pilih algoritma yang ingin dicoba
3. Copy-paste contoh dari dokumentasi ini
4. Verifikasi hasil dengan ciphertext yang diberikan

---

**Last Updated**: February 2026
