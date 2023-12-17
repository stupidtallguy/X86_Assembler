import time

def start():
    print("<<<Hey!>>>") 
    time.sleep(0.1)
    print("<<<Welcome to Assembler>>>")
    time.sleep(0.1)
    option = int(input("Choose an Option For Assembling : \n1)File\n2)Command"))
    if option == 1:
        assemble_from_file()
    elif option == 2:
        # TODO: Use Command Line to Assemble
        pass
    else :
        print("Wrong input Please Try again!")

def assemble_from_file():
    # document why this method is empty
    pass


binary_to_hex_dict = {
    '0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4',
    '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9',
    '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
}

registers_32bit = {'eax': "000", 'ebx': "011", 'ecx': '001', 'edx': '010', 'esi': '110', 'edi': '111', 'esp': '100',
                   'ebp': '101'}
registers_16bit = {'ax': "000", 'bx': "011", 'cx': '001', 'dx': '010', 'si': '110', 'di': '111', 'sp': '100',
                   'bp': '101'}
registers_8bit = {'al': '000', 'bl': '011', 'cl': '001', 'dl': '010', 'ah': '100', 'bh': '111', 'ch': '101',
                  'dh': '110'}

registers_8bit_MOD00 = {'[al]': '000', '[bl]': '011', '[cl]': '001', '[dl]': '010', '[ah]': '100', '[bh]': '111',
                        '[ch]': '101', '[dh]': '110'}
registers_16bit_MOD00 = {'[ax]': "000", '[bx]': "011", '[cx]': '001', '[dx]': '010', '[si]': '110', '[di]': '111',
                         '[sp]': '100', '[bp]': '101'}
registers_32bit_MOD00 = {'[eax]': "000", '[ebx]': "011", '[ecx]': '001', '[edx]': '010', '[esi]': '110', '[edi]': '111',
                         '[esp]': '100', '[ebp]': '101'}
