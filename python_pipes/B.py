import binascii
import random
import sys
import os
from subprocess import Popen, PIPE

class Result:
    pass

result = Result()
process_A = Popen(['python3', 'A.py', sys.argv[1]], stdout = PIPE)

# things to do while the A process finish
seed = int(sys.argv[1])
empty_str = ""
xor_list = []
key_pos = 0
binary_pos = 0
random.seed(seed)

process_A.wait()
stdout = process_A.communicate()
print(str(stdout[0]))
bin_str = str(stdout[0])

separator_index= bin_str.find(',')
end_index= bin_str.find('.')

len_original_bin = int(bin_str[separator_index+1:end_index])
bin_str = bin_str[2:separator_index]
list_bin_str = list(bin_str)
print(bin_str)
input ()
len_bin_str = len(bin_str)
while(len_bin_str<len_original_bin):
    list_bin_str.insert(0,'0')
    len_bin_str+=1
bin_str =  empty_str.join(list_bin_str)       
if bin_str != "":
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
    if os.path.exists("memory_map"):
        os.remove("memory_map")
else:
    print("ERROR: NO SE DETECTÓ LA ENTRADA DE DATOS")
