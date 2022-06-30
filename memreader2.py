from time import sleep
from ReadWriteMemory import ReadWriteMemory


rwm = ReadWriteMemory()

process = rwm.get_process_by_name('ruffle.exe')
process.open()

offsets = [0x190,0x40,0x330,0x90,0x248,0x28,0x530,0x78,0x1B0,0x10]
offsets.reverse()

# score_pointer = process.get_pointer(0x00A2DB08, offsets=offsets)
score_pointer = process.get_pointer(0x139E38317A0)


while True:
    sleep(1)
    score = process.read(score_pointer)
    print(score)
# score = process.read(score_pointer)

# print(score)