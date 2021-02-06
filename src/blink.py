EEPROM_SIZE = 2 ** 15
CPU_ADDRESSABLE_SPACE = 2 ** 16
OFFSET = CPU_ADDRESSABLE_SPACE - EEPROM_SIZE #0x8000

def bytes(integer):
    return divmod(integer, 0x100)

def ToCPUAddress(integer):
    return integer + OFFSET

def ToROMAddress(integer):
    return integer - OFFSET


code = bytearray([
    0xa9, 0xff,         # lda #$ff
    0x8d, 0x02, 0x60,   # sta $6002
 
    0xa9, 0x55,         # lda #$55
    0x8d, 0x00, 0x60,   # sta $6000
 
    0xa9, 0xaa,         # lda #$aa
    0x8d, 0x00, 0x60,   # sta $6000
 
    0x4c, 0x05, 0x80    # jmp $8005

])

NO_OP_INSTRUCTION = 0xea
rom = code + bytearray([NO_OP_INSTRUCTION] * (EEPROM_SIZE - len(code)))

CPU_START_ADDRESS = ToCPUAddress(0x0)
CPU_START_HIGH, CPU_START_LOW = bytes(CPU_START_ADDRESS) #0x80, 0x00

CPU_INIT_VECTOR = [0xfffc, 0xfffd]
rom[ToROMAddress(CPU_INIT_VECTOR[0])] = CPU_START_LOW
rom[ToROMAddress(CPU_INIT_VECTOR[1])] = CPU_START_HIGH


with open("./builds/blink.bin", "wb") as out_file:
    out_file.write(rom)