from key_generation import *

def permutation(key,indices):
    return key[indices]


def create_matrix(array):
    return np.matrix(divide_2_parts(array))

def xor(a,b):
    return np.logical_xor(a,b)

def switch(a):
    a,b = divide_2_parts(a)
    return np.concatenate([b,a])


def generate_fk(bloc,k):
    ip_permutation = permutation(bloc, [1, 5, 2, 0, 3, 7, 4, 6])
    right_block = divide_2_parts(ip_permutation)[1]
    right_block_concatenate = np.concatenate((right_block,right_block),axis=0)
    e_p = permutation(right_block_concatenate,[3,0,1,2,1,2,3,0])
    n = create_matrix(e_p)
    k_matrix = create_matrix(k)
    p = xor(n,k_matrix)

    indices_matrix = [((0,1),(0,2)),((0,0),(0,3)),((1,1),(1,2)),((1,0),(1,3))]
    s_temp = []
    s = []

    for indice in indices_matrix:
        s_temp.append(p[indice]*1)



    for element in np.squeeze(s_temp, axis=0):
        str_result = str(element[0])+str(element[1])
        s.append(int(str_result,2))

    s0 = np.matrix([[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]])
    s1 = np.matrix([[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]])

    #Issue to SOLVE
    s[3] = 3


    a = s0[s[1],s[0]]
    b = s1[s[3],s[2]]

    a = "{0:b}".format(a)
    b = "{0:b}".format(b)
    r_8 = np.concatenate([np.array(bitarray(a).tolist()),np.array(bitarray(b).tolist())],axis=0)
    r_9 = permutation(r_8,[1,3,2,0])
    left_block = divide_2_parts(ip_permutation)[0]
    r_10 = xor(left_block,r_9)
    r_11 = np.concatenate([r_10,right_block])
    return(r_11)
