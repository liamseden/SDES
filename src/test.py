from encryption import *

key = '1010000010'
message = '10111101'
message = np.array(bitarray(message).tolist())

k1,k2 = generate_k1_k2(key)
print("K1")
showMessage(k1)

fk_k1 = generate_fk(message,k1)
print("FK 1 ")
showMessage(fk_k1)
print("FK 1 Swicth result")
showMessage(switch(fk_k1))
