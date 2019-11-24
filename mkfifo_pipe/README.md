# shared_memory using named pipes in python
A.py and B.py are non-related processes than can share information thanks to the fifo file, this method also fix the synchronization problem easily thanks to the properties of the fifo file, that consists in keep the first progress that access to it waiting until another process wants to access to the same file, then it gave the permission to the process that needs to write in the file, and then to the process that needs to read.

Example (can be like this or vice-versa):  
Bash 1:  
´
$ python3 B.py 16
´
Bash 2:  
´
$ python3 A.py 16
´