from encryption import *

#Decipher a bloc
def decrypt_bloc(bloc,k1,k2):
    ip_Cypher = permutation_ip(bloc)
    fk1_Cypher  = generate_fk(ip_Cypher,k2)
    fk1_Cypher_Switch = switch(fk1_Cypher)
    fk2_Cypher  = generate_fk(fk1_Cypher_Switch,k1)
    return permutation_ip1(fk2_Cypher)


