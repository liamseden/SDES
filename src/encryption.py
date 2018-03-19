from key_generation import *

def permutation(key,indices):
    return key[indices]

def permutation_ip (bloc):
    return bloc[[1,5,2,0,3,7,4,6]]

def permutation_ip1 (bloc):
    return bloc[[3,0,2,4,6,1,7,5]]

def permutation_P4 (bloc):
    return bloc[[1,3,2,0]]

def permutation_EP (bloc):
    return bloc[[3,0,1,2,1,2,3,0]]

def create_matrix(array):
    return np.matrix(divide_2_parts(array))

def xor(a,b):
    return np.logical_xor(a,b)

def switch(a):
    a,b = divide_2_parts(a)
    return np.concatenate([b,a])


def str2bits (n):
    result = "{0:b}".format(n)
    if (len(result)==1):
        return "0"+result
    return result

def generate_fk(ip_permutation,k):
    right_block = divide_2_parts(ip_permutation)[1]
    right_block_concatenate = np.concatenate((right_block,right_block),axis=0)
    e_p = permutation_EP(right_block_concatenate)
    n = create_matrix(e_p)
    k_matrix = create_matrix(k)
    p = xor(n,k_matrix)

    indices_matrix = [0,1,0,2,0,0,0,3,1,1,1,2,1,0,1,3]
    s_temp = []
    s = []

    for i in range(0, len(indices_matrix), 4):
        s_temp.append(p[indices_matrix[i], indices_matrix[i + 1]] * 1)
        s_temp.append(p[indices_matrix[i + 2], indices_matrix[i + 3]] * 1)

    for i in range(0, len(s_temp), 2):
        str_result = str(s_temp[i]) + str(s_temp[i + 1])
        s.append(int(str_result, 2))

    s0 = np.matrix([[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]])
    s1 = np.matrix([[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]])

    a = s0[s[1],s[0]]
    b = s1[s[3],s[2]]

    a = str2bits(a)
    b = str2bits(b)

    r_8 = np.concatenate([np.array(bitarray(a).tolist()),np.array(bitarray(b).tolist())],axis=0)
    r_9 = permutation_P4(r_8)
    left_block = divide_2_parts(ip_permutation)[0]
    r_10 = xor(left_block,r_9)
    r_11 = np.concatenate([r_10,right_block])
    return(r_11)


def encrypt_bloc (bloc,key):
    k1, k2 = generate_k1_k2(key)
    message = np.array(bitarray(bloc).tolist())
    messageIP = permutation_ip(message)
    fk_k1 = generate_fk(messageIP, k1)
    switch_fk_k1 = switch(fk_k1)
    fk_k2 = generate_fk(switch_fk_k1, k2)
    return permutation_ip1(fk_k2)

#Encrypt with S-DES a ASCII string
def encrypt_message (message,key):
    result = np.array([],dtype=bool)
    for character in message:
        binaryChar = text_to_bits(character)
        test = encrypt_bloc(binaryChar, key)
        result = np.concatenate((result, test), axis=0)
    return result

