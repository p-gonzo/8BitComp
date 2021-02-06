EEPROM_SIZE = 32768

rom = bytearray([0xea] * EEPROM_SIZE)

with open("./builds/no_op.bin", "wb") as out_file:
    out_file.write(rom)