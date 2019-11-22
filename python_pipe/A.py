import random
import binascii
import sys
import pipes

phrase = input('Adquiriendo datos de la entrada estándar\n')
seed = int(sys.argv[1])
bin_str =  '0'+bin(int.from_bytes(phrase.encode(), 'big'))[2:].zfill(8)
list_bin_str = list(bin_str)
random.seed(seed)
random_key = random.getrandbits(len(bin_str))
key= '{0:0b}'.format(random_key)
list_key = list(key)
lenght_key = len(key)
lenght_binary = len(bin_str)
while lenght_key < lenght_binary :
        list_key.insert(0,'0')
        lenght_key+=1
empty_str = ""
key = empty_str.join(list_key)
xor_list = []
key_pos = 0
binary_pos = 0
for binary_content in list_bin_str:
    if list_bin_str[binary_pos] != list_key[key_pos]:
        xor_list.append("1")
    else:
        xor_list.append("0")
    binary_pos +=1
    key_pos +=1
xor_str = empty_str.join(xor_list)
t = pipes.Template()
f = t.open('pipe', 'w')
f.write(xor_str)
f.close()