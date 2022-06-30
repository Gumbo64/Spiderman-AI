from importlib.util import module_from_spec
from time import sleep
from pymem import *
from pymem.process import *

import os
import subprocess
subprocess.Popen(["ruffle.exe", "spiderman.swf"])
# os.system('cmd /c "./'+os.getcwd()+'./ruffle.exe spiderman.swf"')


sleep(4)

mem = Pymem("ruffle.exe")

module = module_from_name(mem.process_handle,"ruffle.exe").lpBaseOfDll
print(module)
offsets = [0x190,0x40,0x330,0x90,0x248,0x28,0x530,0x78,0x1B0,0x10]
offsets.reverse()

def getPtrAddr(address, offsets):
    addr = mem.read_longlong(address)
    for offset in offsets:
        if offset != offsets[-1]:
            addr = mem.read_longlong(addr + offset)
    addr = addr + offsets[-1]
    return addr


def get_score():
    score_addr = getPtrAddr(module + 0x00A2DB08,offsets)
    score = mem.read_double(score_addr)
    return score

lastscore = 0
counter=0
while True:
    sleep(0.01)
    try:
        score = get_score()
        if(score == lastscore):
            raise Exception("a")
        print(score)
        print(counter)
        counter=0
        
    except:
        counter+=1
        score = lastscore
        # print(counter)
    
    lastscore=score
