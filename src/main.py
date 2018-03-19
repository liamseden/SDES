from decryption import *

key = '1010000010'
message = '01000001'
message = np.array(bitarray(message).tolist())

k1,k2 = generate_k1_k2(key)
print("K1");showMessage(k1)
print("K2");showMessage(k2)

cipher = encrypt_bloc(message,k1,k2)
print("Encrypted message");showMessage(cipher)
decryptedM = decrypt_bloc(cipher,k1,k2)
print("Decrypted message");showMessage(decryptedM)
