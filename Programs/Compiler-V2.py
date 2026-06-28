import re
from pathlib import Path

# ================================================================================================
# ::                                                                                            ::
# ::           NOVA COMPILER V2.0 :: Nova Assembly HIGH to Nova MAC [BASE 10 BINARY]            ::
# ::                                                                                            ::
# ::  This is Version 2 of the Compiler, it is a complete rewrite of the original Compiler.py   ::
# ::                                                                                            ::
# ================================================================================================


## TODO: ##
# Add more complex premade operations like 'IF()'
# Load programs from Files
# Write Programs to Files
# Search File for Errors on Compile (Compilation errors like a jailbroken cpu)

## SCHEME/CODE LAYOUT ##
# ~ user data (file to write to / copy, level to compile to (ASM, MAC, BIN10), DEBUG, etc)
# Y user Code (or a file to read from in the future)
# Y Ls 2Opcodes, Ls 1Opcodes, Ls 0Opcodes, Ls , Ls Registers ##(adds functionality for 11 registers for example, or simple 2ops, through {part[1] in 1OP?})
# Compile code
## Y grab code into a list (from a file or from user input)
## Y init values (labels as [])
           ####### ~ add functions in future to add more usage IE: IF modifies at this step from ASM to MAC
## Y remove null strings (comments (all but a character to start a line), blanks, etc)
## Y expand JMP Commands to include the address (J) before in a MOVI, MOVI J {Label}
## Y find labels and replace them with the correct address (J) in a MOVI, eg: MOVI J loop -> MOVI J 100
## Y find registers and replace them with the correct address (R) in a MOVI, eg: MOVI A 0 -> MOVI 0 0
## Y replace all {label} + ":" with nothing, eg: loop: -> "0000"
## Y search for all opcodes and replace them with the correct hex value, eg: MOVI -> 02, NOP -> 00, etc
## Y Remove all spaces
# Y write code list to output

# V User Options V

# if using copy/paste, program/paste your assembly below read 
# " https://github.com/Blackhole-Studios/NOVA/blob/main/Documentation/ISA.md " 
# for Documentation on how to write ASM code.

file_to_use = "test.asm" # in progress
file_to_write = "test.bin" # in progress
use_file = False # write to and read from file. good for when compiling 100+ lines
lang_to_compile_to = "MAC" #machine is the only one supported ATM
DEBUG_MODE = True # prints a snapshot of each step to find errors in your code, or whenever modifing the code, as well prints a copy of the code w/ a line counter
user_code = """

# enter code below
HALT
"""
# code state: js kinda stops
# ^ User Options ^



### START OTHER CODE SECTION ###
# OC Values:
pass
# OC Functions:
pass
### END OTHER CODE SECTION ###


### START MACHINE CODE SECTION ###
# MAC Values 
Op2 = {
    "MOV":  "01",
    "MOVI": "02",
    "READ": "03",
    "STORE":"04",
    "ADD":  "07",
    "SUB":  "08",
    "MUL":  "09",
    "DIV":  "10",
    "MOD":  "11",
    "CMP":  "12",
    "AND":  "13",
    "OR":   "14",
    "IN":   "25"}
Op1 = {
    "PUSH": "05",
    "POP":  "06",
    "JMP":  "16",
    "JZ":   "17",
    "JNZ":  "18",
    "JG":   "19",
    "JL":   "20",
    "INC":  "26",
    "NOT":  "15",
    "CALL": "21",
    "INT":  "23"}
Op0 = {
    "NOP":  "00",
    "RET":  "22",
    "HALT": "27",
    "IRET": "24"}
Reg = {
    "A": "0",
    "B": "1",
    "C": "2",
    "D": "3",
    "E": "4",
    "F": "5",
    "G": "6",
    "H": "7",
    "I": "8",
    "J": "9"}

# MAC Functions:
def clean_code(code):
    out = []
    i = 0
    while i < len(code):
        if code[i][:1].isalpha():
            out.append(code[i].upper())
        i += 1

    return out
def expand_jmp(code):
    out = []

    i = 0
    while i < len(code):
        sp = code[i].split()
        if sp[0] in {"JMP", "JZ", "JNZ", "JG", "JL"}:
            if not (len(sp[1]) == 1 and sp[1].isalpha()):
                out.append(f"MOVI J {sp[1]}")
                out.append(f"{sp[0]} J")
            else:
                out.append(code[i])
        else:
            out.append(code[i])

        i += 1
    
    return out
def define_labels(code):
    out = {}
    i = 0
    while i < len(code):
        sp = code[i].split()
        if (len(sp) == 1 and sp[0].endswith(":")):
            label = sp[0].removesuffix(":")
            out[label] = i+1
        i += 1
    return out
def replace_labels(code, labels):
    out = []
    i = 0
    while i < len(code):
        sp = code[i].split()
        string_builder = ""
        # we only compare it to 3 as the CPU doesn't support more than 3 paramenters formula (OPCODE)[C1, C2], RegisterA[C3], Everything else[C4...]
        if len(sp) == 3:
            #part 1
            if sp[0] in labels:
                string_builder = "" + str(labels[sp[0]])
            else:
                string_builder = "" + str(sp[0])
            
            # part 2
            if sp[1] in labels:
                string_builder = string_builder + " " + str(labels[sp[1]])
            else:
                string_builder = string_builder + " " + str(sp[1])

            #part 3
            if sp[2] in labels:
                string_builder = string_builder + " " + str(labels[sp[2]])
            else:
                string_builder = string_builder + " " + str(sp[2])

        elif len(sp) == 2:
            #part 1
            if sp[0] in labels:
                string_builder = "" + str(labels[sp[0]])
            else:
                string_builder = "" + str(sp[0])

            # part 2
            if sp[1] in labels:
                string_builder = string_builder + " " + str(labels[sp[1]])
            else:
                string_builder = string_builder + " " + str(sp[1])

        else:
            #part 1
            if sp[0].endswith(":"):
                string_builder = "NOP"
            else:
                string_builder = "" + str(sp[0])
        out.append(string_builder)
        i += 1
    return out
def replace_registers(code):
    out = []
    i = 0
    while i < len(code):
        sp = code[i].split()
        string_builder = ""
        # we only compare it to 3 as the CPU doesn't support more than 3 paramenters formula (OPCODE)[C1, C2], RegisterA[C3], Everything else[C4...]
        if len(sp) == 3:
            #part 1
            if sp[0] in Reg:
                string_builder = "" + str(Reg[sp[0]])
            else:
                string_builder = "" + str(sp[0])
            # part 2
            if sp[1] in Reg:
                string_builder = string_builder + " " + str(Reg[sp[1]])
            else:
                string_builder = string_builder + " " + str(sp[1])
            #part 3
            if sp[2] in Reg:
                string_builder = string_builder + " " + str(Reg[sp[2]])
            else:
                string_builder = string_builder + " " + str(sp[2])
        elif len(sp) == 2:
            #part 1
            if sp[0] in Reg:
                string_builder = "" + str(Reg[sp[0]])
            else:
                string_builder = "" + str(sp[0])
            # part 2
            if sp[1] in Reg:
                string_builder = string_builder + " " + str(Reg[sp[1]])
            else:
                string_builder = string_builder + " " + str(sp[1])
        else:
            if sp[0] in Reg:
                string_builder = "" + str(Reg[sp[0]])
            else:
                string_builder = "" + str(sp[0])
        out.append(string_builder)
        i += 1
    return out
def replace_opcodes(code):
    out = []
    i = 0
    while i < len(code):
        sp = code[i].split()
        if len(sp) > 0:
            if sp[0] in Op0:
                if len(sp) == 1:
                    out.append(str(Op0[sp[0]]) + "00")
                else:
                    return f"ERROR: Incorrect # arguments {code[i]}"

            elif sp[0] in Op1:
                if len(sp) == 2:
                    out.append(str(Op1[sp[0]]) + " " + str(sp[1]))
                else:
                    return f"ERROR: Incorrect # arguments {code[i]}"

            elif sp[0] in Op2:
                if len(sp) == 3:
                    out.append(str(Op2[sp[0]]) + " " + str(sp[1]) + " " + str(sp[2]))
                else:
                    return f"ERROR: Incorrect # arguments {code[i]}"
        else:
            continue
        i += 1
    return out
def remove_spaces(code):
    out = []
    i = 0
    while i < len(code):
        sp = code[i].split()
        if len(sp) == 1:
            out.append(str(sp[0]))
        elif len(sp) == 2:
            out.append(str(sp[0]) + str(sp[1]))
        else:
            out.append(str(sp[0]) + str(sp[1]) + str(sp[2]))
        i += 1

    return out
def MAC_COMPILE_CODE(code_list):
    if DEBUG_MODE:
        print("Current Code [pre Cleaner]: " + str(code_list))
    
    code_list = clean_code(code_list)
    
    if DEBUG_MODE:
        print("Current Code [pre MOVI add]: " + str(code_list))

    code_list = expand_jmp(code_list)

    # after this point, no more lines are added NOR subtracted, it's a fixed size now

    if DEBUG_MODE:
        print("Current Code [pre label rep]: " + str(code_list))

    labels = define_labels(code_list)

    if DEBUG_MODE:
        print("JMP Labels: " + str(labels))

    code_list = replace_labels(code_list, labels)

    if DEBUG_MODE:
        print("Current Code [pre register rep]: " + str(code_list))

    code_list = replace_registers(code_list)

    if DEBUG_MODE:
        print("Current Code [pre opCode rep]: " + str(code_list))

    code_list = replace_opcodes(code_list)

    if DEBUG_MODE:
        print("Current Code [pre SPACE del]: " + str(code_list))

    code_list = remove_spaces(code_list)

    if DEBUG_MODE:
        print("Final Code: " + str(code_list) + "\n")

    return code_list
### END MACHINE CODE SECTION ###



# managers:
if use_file == False:
    code_list = [y for y in (x.strip() for x in user_code.splitlines()) if y]
else:
    pass # pull from a file


if lang_to_compile_to == "MAC":
    code = MAC_COMPILE_CODE(code_list)
else:
    pass # open source?

if DEBUG_MODE:
    for i in range(len(code)):
        print(str(i+1) + ". " + code[i])
if use_file == False:
    print("FINAL COMPILED CODE: \n")
    for i in code:
        print(i)
    print("\nCopy The above code and paste it into whatever.")
else:
    # write to file . script
    print(f"Compiled code was written to file {file_to_write}")
