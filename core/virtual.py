from core.colors import *
import os
import sys
from time import sleep as ts
print(Y+"master install virtual kali linux"+W)
os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh")
os.system("./start-kali.sh")
print(G+"complete"+W)