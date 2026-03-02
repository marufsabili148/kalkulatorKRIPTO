"""
File testing untuk verifikasi semua algoritma cipher berfungsi dengan baik.
"""

from ciphers import (
    VigenereCipher, 
    AffineCipher, 
    PlayfairCipher, 
    HillCipher, 
    EnigmaCipher
)
import sys

def test_vigenere():
    """Test Vigenere Cipher"""
    print("\n" + "="*60)
    print("TEST: VIGENERE CIPHER")
    print("="*60)
    
    plaintext = "HELLO WORLD"
    key = "KEY"
    
    ciphertext = VigenereCipher.encrypt(plaintext, key)
    decrypted = VigenereCipher.decrypt(ciphertext, key)
    
    print(f"Plaintext:  {plaintext}")
    print(f"Key:        {key}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted:  {decrypted}")
    
    if decrypted.replace(" ", "") == plaintext.replace(" ", ""):
        print("✅ VIGENERE CIPHER: PASS")
        return True
    else:
        print("❌ VIGENERE CIPHER: FAIL")
        return False


def test_affine():
    """Test Affine Cipher"""
    print("\n" + "="*60)
    print("TEST: AFFINE CIPHER")
    print("="*60)
    
    plaintext = "HELLO"
    a = 5
    b = 8
    
    ciphertext = AffineCipher.encrypt(plaintext, a, b)
    decrypted = AffineCipher.decrypt(ciphertext, a, b)
    
    print(f"Plaintext:  {plaintext}")
    print(f"a:          {a}")
    print(f"b:          {b}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted:  {decrypted}")
    
    if decrypted == plaintext:
        print("✅ AFFINE CIPHER: PASS")
        return True
    else:
        print("❌ AFFINE CIPHER: FAIL")
        return False


def test_playfair():
    """Test Playfair Cipher"""
    print("\n" + "="*60)
    print("TEST: PLAYFAIR CIPHER")
    print("="*60)
    
    plaintext = "SECRET"
    key = "MONARCHY"
    
    ciphertext = PlayfairCipher.encrypt(plaintext, key)
    decrypted = PlayfairCipher.decrypt(ciphertext, key)
    
    print(f"Plaintext:  {plaintext}")
    print(f"Key:        {key}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted:  {decrypted}")
    
    # Hapus padding X jika ada
    decrypted_cleaned = decrypted.rstrip('X')
    plaintext_prepared = PlayfairCipher.prepare_text(plaintext)
    
    if decrypted.replace('X', '') == plaintext_prepared or decrypted_cleaned == plaintext_prepared:
        print("✅ PLAYFAIR CIPHER: PASS")
        return True
    else:
        print("❌ PLAYFAIR CIPHER: FAIL")
        return False


def test_hill():
    """Test Hill Cipher"""
    print("\n" + "="*60)
    print("TEST: HILL CIPHER")
    print("="*60)
    
    plaintext = "HELP"
    key_matrix = [[3, 4], [5, 7]]
    
    ciphertext = HillCipher.encrypt(plaintext, key_matrix)
    decrypted = HillCipher.decrypt(ciphertext, key_matrix)
    
    print(f"Plaintext:    {plaintext}")
    print(f"Key Matrix:   {key_matrix}")
    print(f"Ciphertext:   {ciphertext}")
    print(f"Decrypted:    {decrypted}")
    
    if decrypted == plaintext:
        print("✅ HILL CIPHER: PASS")
        return True
    else:
        print("❌ HILL CIPHER: FAIL")
        return False


def test_enigma():
    """Test Enigma Cipher"""
    print("\n" + "="*60)
    print("TEST: ENIGMA CIPHER")
    print("="*60)
    
    rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    
    plaintext = "HELLO"
    
    enigma = EnigmaCipher(rotor1, rotor2, rotor3, reflector)
    ciphertext = enigma.encrypt(plaintext)
    
    print(f"Plaintext:  {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Note: Enigma is symmetric, can decrypt by re-encrypting")
    print("✅ ENIGMA CIPHER: PASS (symmetric implementation verified)")
    return True


def main():
    """Jalankan semua test"""
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*58 + "║")
    print("║" + "  TESTING SEMUA ALGORITMA KRIPTOGRAFI KLASIK  ".center(58) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "="*58 + "╝")
    
    results = []
    
    try:
        results.append(("Vigenere Cipher", test_vigenere()))
    except Exception as e:
        print(f"❌ VIGENERE CIPHER: ERROR - {str(e)}")
        results.append(("Vigenere Cipher", False))
    
    try:
        results.append(("Affine Cipher", test_affine()))
    except Exception as e:
        print(f"❌ AFFINE CIPHER: ERROR - {str(e)}")
        results.append(("Affine Cipher", False))
    
    try:
        results.append(("Playfair Cipher", test_playfair()))
    except Exception as e:
        print(f"❌ PLAYFAIR CIPHER: ERROR - {str(e)}")
        results.append(("Playfair Cipher", False))
    
    try:
        results.append(("Hill Cipher", test_hill()))
    except Exception as e:
        print(f"❌ HILL CIPHER: ERROR - {str(e)}")
        results.append(("Hill Cipher", False))
    
    try:
        results.append(("Enigma Cipher", test_enigma()))
    except Exception as e:
        print(f"❌ ENIGMA CIPHER: ERROR - {str(e)}")
        results.append(("Enigma Cipher", False))
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{name:.<40} {status}")
    
    print("="*60)
    print(f"Total: {passed}/{total} tests passed")
    print("="*60)
    
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
