from encryption import *

#Decipher a bloc
def decrypt_bloc(bloc,key):
    k1, k2 = generate_k1_k2(key)
    ip_Cypher = permutation_ip(bloc)
    fk1_Cypher  = generate_fk(ip_Cypher,k2)
    fk1_Cypher_Switch = switch(fk1_Cypher)
    fk2_Cypher  = generate_fk(fk1_Cypher_Switch,k1)
    return permutation_ip1(fk2_Cypher)


#Decipher an encrypted S-DES message and returns the decrypted bit code and ascii code
def decrypt_message(message,key):
    result = ""
    for bloc in range (0,len(message),8):
        a = decrypt_bloc(message[bloc:bloc+8],key)
        str1 = ''.join(str(e) for e in a*1)
        result += str1
    return text_from_bits(result),result
