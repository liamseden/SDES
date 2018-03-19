from decryption import *
print "Example with one bloc :"
#Example with 1 bloc
key = '1010000010'
message = '01000001'

cipher = encrypt_bloc(message,key)
print("-> Encrypted bloc");
print_code(cipher)

decryptedM = decrypt_bloc(cipher,key)
print("-> Decrypted bloc");
print_code(decryptedM)

print "\n\n\nExample with a string :"
#Example with 1 string
msg = 'Creative'
key = '1010000010'

cipher = encrypt_message(msg,key)
print("1a- Encrypted message");
print text_from_bits(''.join(str(e) for e in cipher*1))
print("1b- Binary Encrypted message");
print_code(cipher)

clear_message,clear_ascii = decrypt_message(cipher,key)
print("\n2a- Decrypted message");print(clear_message);
print("2b- Binary decrypted message");print(clear_ascii)