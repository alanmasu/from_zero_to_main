from elftools.elf.elffile import ELFFile
import sys

def bytes_to_coe(data, base_addr, endian='little'):
    if endian not in ['little', 'big']:
        raise ValueError("Endianness must be 'little' or 'big'")
    
    coe_str = "memory_initialization_radix=16;\nmemory_initialization_vector=\n"
    addr = base_addr
    data_len = len(data)
    
    for i in range(0, data_len, 4):
        if i + 3 < data_len:
            word = data[i:i+4]
        else:
            word = data[i:data_len] + bytes(4 - (data_len - i))  # Pad the remaining bytes to make a 32-bit word
        
        if endian == 'big':
            word = word[::-1]  # Reverse the byte order for big-endian
        
        word_str = "".join(f"{byte:02X}" for byte in word)
        coe_str += f"{word_str},\n"
        addr += 4
        
    coe_str = coe_str[:-2] + ";\n"  # Replace the last comma with a semicolon
    return coe_str

def extract_sections(elf, section_names):
    data = bytearray()
    for section_name in section_names:
        section = elf.get_section_by_name(section_name)
        if section is not None:
            data.extend(section.data())
        else:
            print(f"Section {section_name} not found in elf file")
    return data

def write_coe(filename, data, base_addr, endian):
    with open(filename, 'w') as f:
        coe_data = bytes_to_coe(data, base_addr, endian)
        f.write(coe_data)

def main(elf_filename):
    # Define sections for ROM and RAM
    rom_sections = ['.text', '.rodata']  # Sections to include in ROM COE
    ram_sections = ['.data', '.bss']     # Sections to include in RAM COE
    
    # Define endianness
    rom_endian = 'big'  # or 'little'
    ram_endian = 'big'  # or 'little'

    # Output file names
    rom_coe_filename = 'build/rom.coe'
    ram_coe_filename = 'build/ram.coe'

    with open(elf_filename, 'rb') as f:
        elf = ELFFile(f)
        
        rom_data = extract_sections(elf, rom_sections)
        ram_data = extract_sections(elf, ram_sections)

        if rom_data:
            write_coe(rom_coe_filename, rom_data, 0x40000000, rom_endian)
        else:
            print(f"No ROM sections found in {elf_filename}")

        if ram_data:
            write_coe(ram_coe_filename, ram_data, 0x40010000, ram_endian)
        else:
            print(f"No RAM sections found in {elf_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input.elf>")
        print("Example: elf_to_coe.py input.elf")
    else:
        main(sys.argv[1])
