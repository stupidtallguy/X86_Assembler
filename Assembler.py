import time
import re


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

def print_hex_offsets(used_bytes_list):
    offset = 0
    for used_bytes in used_bytes_list:
        # Ensure a total of 16 digits with leading zeros
        hex_offset = format(offset, f'0{16}X')
        print(f"0x{hex_offset}:")
        offset += used_bytes


def convertFunc(number):
    return (binary_to_hex_dict[number[0][0:4]] + binary_to_hex_dict[number[0][4:8]] + " " +
     binary_to_hex_dict[number[0][8:12]] + binary_to_hex_dict[number[0][12:16]])


def convertFunc2(number):
    return (binary_to_hex_dict[number[0][0:4]] +
          binary_to_hex_dict[number[0][4:8]])


def convert16Func2(number):
    return ('66 ' + binary_to_hex_dict[number[0]
          [0:4]] + binary_to_hex_dict[number[0][4:8]])


def convert16Func(number):
    return ('66 ' + binary_to_hex_dict[number[0][0:4]] + binary_to_hex_dict[number[0][4:8]] +
          binary_to_hex_dict[number[0][8:12]] + binary_to_hex_dict[number[0][12:16]])


def assemble(instruction, first_arg, second_arg):
    if first_arg in registers_32bit and second_arg in registers_32bit:
        number.append(instructionOpcode[instruction]+'01' + '11' +
                      registers_32bit[second_arg]+registers_32bit[first_arg])
        return convertFunc(number)
    elif first_arg in registers_16bit and second_arg in registers_16bit:
        number.append(instructionOpcode[instruction]+'01' + '11' +
                      registers_16bit[second_arg]+registers_16bit[first_arg])
        return convert16Func(number)
    elif first_arg in registers_8bit and second_arg in registers_8bit:
        number.append(instructionOpcode[instruction] + '00' + '11' +
                      registers_8bit[second_arg] + registers_8bit[first_arg])
        return convertFunc(number)
    elif first_arg in registers_32bit_MOD00 and second_arg in registers_32bit:
        number.append(instructionOpcode[instruction] + '01' + '00' +
                      registers_32bit[second_arg] + registers_32bit_MOD00[first_arg])
        return convertFunc(number)
    elif first_arg in registers_32bit_MOD00 and second_arg in registers_16bit:
        number.append(instructionOpcode[instruction] + '01' + '00' +
                      registers_16bit[second_arg] + registers_32bit_MOD00[first_arg])
        return convert16Func(number)
    elif first_arg in registers_32bit_MOD00 and second_arg in registers_8bit:
        number.append(instructionOpcode[instruction] + '00' + '00' +
                      registers_8bit[second_arg] + registers_32bit_MOD00[first_arg])
        return convertFunc(number)
    elif first_arg in registers_32bit and second_arg in registers_32bit_MOD00:
        number.append(instructionOpcode[instruction] + '11' + '00' +
                      registers_32bit[first_arg] + registers_32bit_MOD00[second_arg])
        return convertFunc(number)
    elif first_arg in registers_16bit and second_arg in registers_32bit_MOD00:
        number.append(instructionOpcode[instruction] + '11' + '00' +
                      registers_16bit[first_arg] + registers_32bit_MOD00[second_arg])
        return convert16Func(number)
    elif first_arg in registers_8bit and second_arg in registers_32bit_MOD00:
        number.append(instructionOpcode[instruction] + '10' + '00' +
                      registers_8bit[first_arg] + registers_32bit_MOD00[second_arg])
        return convertFunc(number)
    elif first_arg in registers_32bit:
        number.append(
            instructionOpcode[instruction] + registers_32bit[first_arg])
        return convertFunc2(number)
    elif first_arg in registers_16bit:
        number.append(
            instructionOpcode[instruction] + registers_16bit[first_arg])
        return convert16Func2(number)

def assemble_from_file():
    file_path = input("Please Enter Your File Path To Assemble: ")
    with open(file_path, 'r') as file : #Opening file to assemble
        code = file.read()
    #Spliting each line and get the instructions and ...
    lines = code.split('\n')
    offset = 0
    offsets = [] 
    for line in lines:
        if line != '':
            
            number = []
            component = re.split(r'\s|,\s*', line)
            instruction = component[0].upper
            arg1 = component[1]
            arg2 = component[2] if len(components) > 2 else None
            hex_offset = format(offset, f'0{16}X')
            s = assemble(instruction,arg1,arg2)
            increase = len(s.replace(" ","")) // 2
            print(f"0x{hex_offset}:" + s)
            hex_offset += increase




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
instructionOpcode = {
    'ADD': '000000', 'SUB': '001010', 'AND': '001000', 'OR': '000010', 'XOR': '001100', 'PUSH': '01010',
    'POP': '01011', 'INC': '01000', 'DEC': '01001'
}
