import binascii
import random
import sys

seed = int(sys.argv[1])
empty_str = ""
xor_list = []
key_pos = 0
binary_pos = 0
random.seed(seed)

#reading from the named pipe
fifo = open("./mkpipe", "r")
bin_str = fifo.read()
fifo.close()
list_bin_str = list(bin_str)
print("Texto Encriptado: \n" + bin_str)

random_key = random.getrandbits(len(bin_str))
key= '{0:0b}'.format(random_key)
list_key = list(key)
lenght_key = len(key)
lenght_bin = len(bin_str)
while lenght_key < lenght_bin :
       list_key.insert(0,'0')
       lenght_key+=1

key = empty_str.join(list_key)


for binary_content in list_bin_str:
    if list_bin_str[binary_pos] != list_key[key_pos]:
        xor_list.append("1")
    else:
        xor_list.append("0")
    binary_pos +=1
    key_pos +=1
original_bin = empty_str.join(xor_list)
original_string = int('0b'+original_bin,2).to_bytes((int('0b'+original_bin,2).bit_length() + 7) // 8, 'big').decode()
print("Texto Original : " + str(original_string)) 