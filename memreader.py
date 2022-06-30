from importlib.util import module_from_spec
from pymem import *
from pymem.process import *

mem = Pymem("ruffle.exe")

module = module_from_name(mem.process_handle,"ruffle.exe").lpBaseOfDll
print(module)
offsets = [0x190,0x40,0x330,0x90,0x248,0x28,0x530,0x78,0x1B0,0x10]
offsets.reverse()
print(offsets)



# score = mem.read_double(0x139E38317A0)
# print(0x139E38317A0)
# print(score)



def getPtrAddr(address, offsets):
    addr = mem.read_longlong(address)
    for offset in offsets:
        if offset != offsets[-1]:
            addr = mem.read_longlong(addr + offset)
    addr = addr + offsets[-1]
    return addr


score_addr = getPtrAddr(module + 0x00A2DB08,offsets)


score = mem.read_double(score_addr)

print(score)
