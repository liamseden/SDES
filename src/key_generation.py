from bitarray import bitarray
import numpy as np


# Fonction qui prend en parametre la cle et effectue une permutation P10
def permutation_p10(key):
    indices = [2,4,1,6,3,9,0,8,7,5];
    key = np.array(key.tolist())
    key_p10 = key[indices]
    return key_p10

def permetutation_p8(key):
    indices = [5,2,6,3,7,4,9,8];
    return key[indices]


#Divide two parts
def divide_2_parts(key):
    return np.split(key,2)

# Circular left shift
def circular_left_shift(key,depth):
    return np.concatenate((np.roll(key[0], depth),np.roll(key[1], depth)),0)


def generate_k1_k2(key):
    ba = bitarray(key)
    result = permutation_p10(ba)
    split_2_parts = divide_2_parts(result)
    circular_left_shift_result = circular_left_shift(split_2_parts, -1)
    k1 = permetutation_p8(circular_left_shift_result)
    divide_2_parts_circular = divide_2_parts(circular_left_shift_result)
    k2 = permetutation_p8(circular_left_shift(divide_2_parts_circular, -2))
    return(k1,k2)


def showMessage(list):
    show = ""
    for  i  in list :
        if (i == False) :
            show+=" 0"
        else :
            show+=" 1"
    print show


