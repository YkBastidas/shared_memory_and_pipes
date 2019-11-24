# shared_memory_and_pipes
Two programs, the 'A' encrypted program and the 'B' decrypted using an encryption based on converting the string to binary, generating a random key and encrypting the original key by making XOR with the random key. The seed for the random key is entered by command line. - The program 'A' reads by standard input the string of characters to be encrypted. - Program 'B' writes the encrypted string and then the decrypted string in standard output.

In this principal version A.py and B.py can be connected through a PIPE in the bash
Example:
$ python3 A.py 16 | python3 B.py 16
