# Module untuk implementasi algoritma kriptografi klasik

import numpy as np
from typing import Tuple, List
import string

class VigenereCipher:
    """Implementasi Vigenere Cipher"""
    
    @staticmethod
    def prepare_text(text: str) -> str:
        """Siapkan teks dengan menghilangkan karakter non-alfabet"""
        return ''.join(c.upper() for c in text if c.isalpha())
    
    @staticmethod
    def encrypt(plaintext: str, key: str) -> str:
        """Enkripsi menggunakan Vigenere Cipher"""
        plaintext = VigenereCipher.prepare_text(plaintext)
        key = VigenereCipher.prepare_text(key)
        
        if not key:
            return plaintext
        
        ciphertext = []
        key_index = 0
        
        for char in plaintext:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord('A')
                encrypted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                ciphertext.append(encrypted)
                key_index += 1
            else:
                ciphertext.append(char)
        
        return ''.join(ciphertext)
    
    @staticmethod
    def decrypt(ciphertext: str, key: str) -> str:
        """Dekripsi menggunakan Vigenere Cipher"""
        ciphertext = VigenereCipher.prepare_text(ciphertext)
        key = VigenereCipher.prepare_text(key)
        
        if not key:
            return ciphertext
        
        plaintext = []
        key_index = 0
        
        for char in ciphertext:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord('A')
                decrypted = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                plaintext.append(decrypted)
                key_index += 1
            else:
                plaintext.append(char)
        
        return ''.join(plaintext)


class AffineCipher:
    """Implementasi Affine Cipher"""
    
    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Hitung GCD"""
        while b:
            a, b = b, a % b
        return a
    
    @staticmethod
    def mod_inverse(a: int, m: int) -> int:
        """Hitung modular inverse"""
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return None
    
    @staticmethod
    def is_valid_key(a: int) -> bool:
        """Validasi bahwa a dan 26 adalah coprime"""
        return AffineCipher.gcd(a, 26) == 1
    
    @staticmethod
    def prepare_text(text: str) -> str:
        """Siapkan teks"""
        return ''.join(c.upper() for c in text if c.isalpha())
    
    @staticmethod
    def encrypt(plaintext: str, a: int, b: int) -> str:
        """Enkripsi menggunakan Affine Cipher"""
        if not AffineCipher.is_valid_key(a):
            raise ValueError(f"Nilai a={a} tidak valid. gcd(a, 26) harus = 1")
        
        plaintext = AffineCipher.prepare_text(plaintext)
        ciphertext = []
        
        for char in plaintext:
            if char.isalpha():
                x = ord(char) - ord('A')
                encrypted_val = (a * x + b) % 26
                ciphertext.append(chr(encrypted_val + ord('A')))
            else:
                ciphertext.append(char)
        
        return ''.join(ciphertext)
    
    @staticmethod
    def decrypt(ciphertext: str, a: int, b: int) -> str:
        """Dekripsi menggunakan Affine Cipher"""
        if not AffineCipher.is_valid_key(a):
            raise ValueError(f"Nilai a={a} tidak valid. gcd(a, 26) harus = 1")
        
        ciphertext = AffineCipher.prepare_text(ciphertext)
        a_inv = AffineCipher.mod_inverse(a, 26)
        plaintext = []
        
        for char in ciphertext:
            if char.isalpha():
                y = ord(char) - ord('A')
                decrypted_val = (a_inv * (y - b)) % 26
                plaintext.append(chr(decrypted_val + ord('A')))
            else:
                plaintext.append(char)
        
        return ''.join(plaintext)


class PlayfairCipher:
    """Implementasi Playfair Cipher"""
    
    @staticmethod
    def prepare_text(text: str) -> str:
        """Siapkan teks dengan menghilangkan J dan mengganti dengan I"""
        text = ''.join(c.upper() for c in text if c.isalpha())
        text = text.replace('J', 'I')
        return text
    
    @staticmethod
    def prepare_key(key: str) -> str:
        """Siapkan kunci untuk matriks Playfair"""
        key = PlayfairCipher.prepare_text(key)
        seen = set()
        result = []
        
        for char in key:
            if char not in seen:
                result.append(char)
                seen.add(char)
        
        # Tambahkan sisa alfabet
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Tanpa J
        for char in alphabet:
            if char not in seen:
                result.append(char)
        
        return ''.join(result)
    
    @staticmethod
    def create_matrix(key: str) -> List[List[str]]:
        """Buat matriks 5x5 Playfair"""
        key = PlayfairCipher.prepare_key(key)
        matrix = []
        for i in range(5):
            matrix.append(list(key[i*5:(i+1)*5]))
        return matrix
    
    @staticmethod
    def find_position(matrix: List[List[str]], char: str) -> Tuple[int, int]:
        """Cari posisi karakter dalam matriks"""
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == char:
                    return i, j
        return None
    
    @staticmethod
    def prepare_plaintext(text: str) -> str:
        """Siapkan plaintext untuk enkripsi Playfair"""
        text = PlayfairCipher.prepare_text(text)
        # Tambahkan padding X jika panjang ganjil
        if len(text) % 2 == 1:
            text += 'X'
        return text
    
    @staticmethod
    def encrypt(plaintext: str, key: str) -> str:
        """Enkripsi menggunakan Playfair Cipher"""
        plaintext = PlayfairCipher.prepare_plaintext(plaintext)
        matrix = PlayfairCipher.create_matrix(key)
        ciphertext = []
        
        for i in range(0, len(plaintext), 2):
            char1 = plaintext[i]
            char2 = plaintext[i+1] if i+1 < len(plaintext) else 'X'
            
            row1, col1 = PlayfairCipher.find_position(matrix, char1)
            row2, col2 = PlayfairCipher.find_position(matrix, char2)
            
            if row1 == row2:  # Baris sama
                ciphertext.append(matrix[row1][(col1 + 1) % 5])
                ciphertext.append(matrix[row2][(col2 + 1) % 5])
            elif col1 == col2:  # Kolom sama
                ciphertext.append(matrix[(row1 + 1) % 5][col1])
                ciphertext.append(matrix[(row2 + 1) % 5][col2])
            else:  # Rectangle
                ciphertext.append(matrix[row1][col2])
                ciphertext.append(matrix[row2][col1])
        
        return ''.join(ciphertext)
    
    @staticmethod
    def decrypt(ciphertext: str, key: str) -> str:
        """Dekripsi menggunakan Playfair Cipher"""
        ciphertext = PlayfairCipher.prepare_text(ciphertext)
        matrix = PlayfairCipher.create_matrix(key)
        plaintext = []
        
        for i in range(0, len(ciphertext), 2):
            char1 = ciphertext[i]
            char2 = ciphertext[i+1] if i+1 < len(ciphertext) else 'X'
            
            row1, col1 = PlayfairCipher.find_position(matrix, char1)
            row2, col2 = PlayfairCipher.find_position(matrix, char2)
            
            if row1 == row2:  # Baris sama
                plaintext.append(matrix[row1][(col1 - 1) % 5])
                plaintext.append(matrix[row2][(col2 - 1) % 5])
            elif col1 == col2:  # Kolom sama
                plaintext.append(matrix[(row1 - 1) % 5][col1])
                plaintext.append(matrix[(row2 - 1) % 5][col2])
            else:  # Rectangle
                plaintext.append(matrix[row1][col2])
                plaintext.append(matrix[row2][col1])
        
        return ''.join(plaintext)


class HillCipher:
    """Implementasi Hill Cipher"""
    
    @staticmethod
    def matrix_inverse_mod(matrix: np.ndarray, mod: int) -> np.ndarray:
        """Hitung invers matriks dalam modulo"""
        det = int(np.round(np.linalg.det(matrix))) % mod
        
        # Hitung modular inverse dari determinan
        inv_det = None
        for i in range(1, mod):
            if (det * i) % mod == 1:
                inv_det = i
                break
        
        if inv_det is None:
            raise ValueError("Matriks tidak dapat diinversi dalam modulo 26")
        
        # Hitung adjugate matrix
        if matrix.shape[0] == 2:
            adj = np.array([[matrix[1, 1], -matrix[0, 1]],
                           [-matrix[1, 0], matrix[0, 0]]])
        else:
            raise ValueError("Hanya mendukung matriks 2x2")
        
        # Hasil = inv_det * adjugate (mod 26)
        result = (inv_det * adj) % mod
        return result.astype(int)
    
    @staticmethod
    def prepare_text(text: str) -> str:
        """Siapkan teks"""
        return ''.join(c.upper() for c in text if c.isalpha())
    
    @staticmethod
    def text_to_vector(text: str) -> List[int]:
        """Konversi teks ke vektor angka"""
        return [ord(c) - ord('A') for c in text]
    
    @staticmethod
    def vector_to_text(vector: List[int]) -> str:
        """Konversi vektor angka ke teks"""
        return ''.join(chr(x % 26 + ord('A')) for x in vector)
    
    @staticmethod
    def encrypt(plaintext: str, key_matrix: List[List[int]]) -> str:
        """Enkripsi menggunakan Hill Cipher"""
        plaintext = HillCipher.prepare_text(plaintext)
        
        # Padding jika perlu
        if len(plaintext) % 2 == 1:
            plaintext += 'X'
        
        K = np.array(key_matrix, dtype=int)
        ciphertext = []
        
        for i in range(0, len(plaintext), 2):
            plain_vector = np.array([
                ord(plaintext[i]) - ord('A'),
                ord(plaintext[i+1]) - ord('A')
            ], dtype=int).reshape(2, 1)
            
            cipher_vector = (K @ plain_vector) % 26
            ciphertext.append(chr(cipher_vector[0, 0] + ord('A')))
            ciphertext.append(chr(cipher_vector[1, 0] + ord('A')))
        
        return ''.join(ciphertext)
    
    @staticmethod
    def decrypt(ciphertext: str, key_matrix: List[List[int]]) -> str:
        """Dekripsi menggunakan Hill Cipher"""
        ciphertext = HillCipher.prepare_text(ciphertext)
        
        K = np.array(key_matrix, dtype=int)
        K_inv = HillCipher.matrix_inverse_mod(K, 26)
        
        plaintext = []
        
        for i in range(0, len(ciphertext), 2):
            cipher_vector = np.array([
                ord(ciphertext[i]) - ord('A'),
                ord(ciphertext[i+1]) - ord('A')
            ], dtype=int).reshape(2, 1)
            
            plain_vector = (K_inv @ cipher_vector) % 26
            plaintext.append(chr(plain_vector[0, 0] + ord('A')))
            plaintext.append(chr(plain_vector[1, 0] + ord('A')))
        
        return ''.join(plaintext)


class EnigmaCipher:
    """Implementasi Enigma Cipher"""
    
    def __init__(self, rotor1: str, rotor2: str, rotor3: str, reflector: str, plugboard: dict = None):
        """Inisialisasi Enigma dengan rotor dan reflector"""
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.reflector = reflector
        self.plugboard = plugboard or {}
        self.position1 = 0
        self.position2 = 0
        self.position3 = 0
    
    @staticmethod
    def prepare_text(text: str) -> str:
        """Siapkan teks"""
        return ''.join(c.upper() for c in text if c.isalpha())
    
    def rotate_rotors(self):
        """Rotasi rotor (double-stepping mechanism)"""
        self.position1 = (self.position1 + 1) % 26
        if self.position1 == 0:
            self.position2 = (self.position2 + 1) % 26
            if self.position2 == 0:
                self.position3 = (self.position3 + 1) % 26
    
    def apply_plugboard(self, char: str) -> str:
        """Terapkan plugboard substitution"""
        if char in self.plugboard:
            return self.plugboard[char]
        return char
    
    def reverse_plugboard(self, char: str) -> str:
        """Reverse plugboard"""
        for k, v in self.plugboard.items():
            if v == char:
                return k
        return char
    
    def pass_through_rotor(self, char: str, rotor: str, position: int, reverse: bool = False) -> str:
        """Lewatkan karakter melalui rotor"""
        index = ord(char) - ord('A')
        index = (index + position) % 26
        
        if reverse:
            rotor_index = rotor.index(chr(index + ord('A')))
        else:
            rotor_index = ord(rotor[index]) - ord('A')
        
        rotor_index = (rotor_index - position) % 26
        return chr(rotor_index + ord('A'))
    
    def encrypt_char(self, char: str) -> str:
        """Enkripsi satu karakter"""
        self.rotate_rotors()
        
        # Plugboard
        char = self.apply_plugboard(char)
        
        # Forward melalui rotor
        char = self.pass_through_rotor(char, self.rotor1, self.position1)
        char = self.pass_through_rotor(char, self.rotor2, self.position2)
        char = self.pass_through_rotor(char, self.rotor3, self.position3)
        
        # Reflector
        char = self.reflector[ord(char) - ord('A')]
        
        # Backward melalui rotor
        char = self.pass_through_rotor(char, self.rotor3, self.position3, reverse=True)
        char = self.pass_through_rotor(char, self.rotor2, self.position2, reverse=True)
        char = self.pass_through_rotor(char, self.rotor1, self.position1, reverse=True)
        
        # Plugboard reverse
        char = self.reverse_plugboard(char)
        
        return char
    
    def encrypt(self, plaintext: str) -> str:
        """Enkripsi menggunakan Enigma"""
        plaintext = EnigmaCipher.prepare_text(plaintext)
        ciphertext = []
        
        for char in plaintext:
            ciphertext.append(self.encrypt_char(char))
        
        return ''.join(ciphertext)
    
    def decrypt(self, ciphertext: str) -> str:
        """Dekripsi menggunakan Enigma (due to symmetry)"""
        # Reset posisi
        self.position1 = 0
        self.position2 = 0
        self.position3 = 0
        
        return self.encrypt(ciphertext)
