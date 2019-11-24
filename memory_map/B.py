import binascii
import random
import sys
import mmap
<<<<<<< Updated upstream:memory_map(branch)/B.py
import subprocess


# call to  the A process
p = subprocess.Popen(['python.exe', './A.py', sys.argv[1]])
=======
import contextlib
import fcntl
import os
import time
>>>>>>> Stashed changes:memory_map/B.py

# things to do while the A process finish
seed = int(sys.argv[1])
empty_str = ""
xor_list = []
key_pos = 0
binary_pos = 0
random.seed(seed)
loading_text = [".", "..", "...", "   "]
while(1):
    if os.path.exists("memory_map"):
        file_handler= open("memory_map", "r")
        fcntl.flock (file_handler, fcntl.LOCK_EX)
        if(file_handler.readline()==""):
            print("El archivo está vacío y ha sido eliminado")
            bin_str = file_handler.readline()
            fcntl.flock (file_handler, fcntl.LOCK_UN)
            file_handler.close()
            os.remove("memory_map")
        else:
            with contextlib.closing(mmap.mmap(file_handler.fileno(), 0, access=mmap.ACCESS_READ, flags=mmap.MAP_SHARED)) as m:
                bin_str = m.readline().decode()
            fcntl.flock (file_handler, fcntl.LOCK_UN)
            file_handler.close()
            list_bin_str = list(bin_str)
        break
    else:
        i = 0
        while i < 4:
            time.sleep(0.5)
            print ("Esperando Datos"+ loading_text[i], sep=' ', end='\r', flush=True)
            i+=1
        
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
