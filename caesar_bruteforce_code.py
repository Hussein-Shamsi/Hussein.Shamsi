def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - start - shift) % 26 + start)
        else:
            decrypted_text += char
    return decrypted_text

def brute_force_caesar(ciphertext):
    print("Attempting decryption using all possible shifts:\n")
    for shift in range(1, 26):
        decrypted = caesar_decrypt(ciphertext, shift)
        print(f"[Shift {shift:2}] {decrypted}")

encrypted_message = "Wklv lv d whvw phvvdjh"
brute_force_caesar(encrypted_message)
