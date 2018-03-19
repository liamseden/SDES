from encryption import *

key = '1010000010'
message = '10111101'
message = np.array(bitarray(message).tolist())

k1,k2 = generate_k1_k2(key)
print("K1")
print(k1)

fk_k1 = generate_fk(message,k1)
print("FK 1 ")
print(fk_k1)
print("FK 1 Swicth result")
print(switch(fk_k1))

fk_k2 = generate_fk(switch(fk_k1),k2)
print("FK 2 ")
print(fk_k2)
print("\n\n")
print("Message crypte : ")
print(permutation(fk_k2,[3,0,2,4,6,1,7,5]))


'''
print("Permutation 8-bits blocs ")
message = '10111101'
message = np.array(bitarray(message).tolist())

ip_permutation = permutation(message,[1,5,2,0,3,7,4,6])
print(ip_permutation)

right_block = divide_2_parts(ip_permutation)[1]
print(right_block)

right_block_concatenate = np.concatenate((right_block,right_block),axis=0)

print(right_block_concatenate)
e_p = permutation(right_block_concatenate,[3,0,1,2,1,2,3,0])

print("E/P result : ")
print(e_p)

print("N Matrix : ")
n = create_matrix(e_p)
print(n)

print("K matrix : ")
k_matrix = create_matrix(k1)
print(k_matrix)


print("P matrix : ")
p = xor(n,k_matrix)
print(p)

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

print("S boxes : ")
s[3] = 3
print(s)

print("S0 boxe : ")
print(s0)

print("S1 boxe : ")
print(s0)

a = s0[s[1],s[0]]
b = s1[s[3],s[2]]

a = "{0:b}".format(a)
b = "{0:b}".format(b)


print("Step 8 : R8")
r_8 = np.concatenate([np.array(bitarray(a).tolist()),np.array(bitarray(b).tolist())],axis=0)
print(r_8)

print("Step 9 : Result permutation ")
r_9 = permutation(r_8,[1,3,2,0])
print(r_9)

print("Step 10 : ")
left_block = divide_2_parts(ip_permutation)[0]
r_10 = xor(left_block,r_9)
print(r_10)

print("Step 11 : ")
r_11 = np.concatenate([r_10,right_block])
print(r_11)

print("Switch : ")
switch_r11 = np.concatenate([right_block,r_10])
print(switch_r11)


'''