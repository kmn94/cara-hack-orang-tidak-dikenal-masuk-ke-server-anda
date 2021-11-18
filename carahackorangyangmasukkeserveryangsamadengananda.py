import os
import sys
import time

x = "Halo kawan ini hadiahmu dari ku"
os.system("clear")

for f in x:
         sys.stdout.write(f)
         sys.stdout.flush()
         time.sleep(0.1)

time.sleep(1)
os.system("cat /dev/urandom")#hanya work di os kali linux