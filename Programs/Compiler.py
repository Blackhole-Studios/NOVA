import re

# TODO:
# Add more complex premade operations like 'IF()'
#     Load programs from Files
#   Write Programs to Files
# Search File for Errors on Compile (Compilation errors like a jailbroken cpu)

OPCODES = {
    "NOP":  "00",
    "MOV":  "01",
    "MOVI": "02",
    "READ": "03",
    "STORE":"04",
    "PUSH": "05",
    "POP":  "06",
    "ADD":  "07",
    "SUB":  "08",
    "MUL":  "09",
    "DIV":  "10",
    "MOD":  "11",
    "CMP":  "12",
    "AND":  "13",
    "OR":   "14",
    "NOT":  "15",
    "JMP":  "16",
    "JZ":   "17",
    "JNZ":  "18",
    "JG":   "19",
    "JL":   "20",
    "CALL": "21",
    "RET":  "22",
    "INT":  "23",
    "IRET": "24",
    "IN":   "25",
    "INC":  "26",
    "HALT": "27",

    "nop":  "00",
    "mov":  "01",
    "movi": "02",
    "read": "03",
    "store":"04",
    "push": "05",
    "pop":  "06",
    "add":  "07",
    "sub":  "08",
    "mul":  "09",
    "div":  "10",
    "mod":  "11",
    "cmp":  "12",
    "and":  "13",
    "or":   "14",
    "not":  "15",
    "jmp":  "16",
    "jz":   "17",
    "jnz":  "18",
    "jg":   "19",
    "jl":   "20",
    "call": "21",
    "ret":  "22",
    "int":  "23",
    "iret": "24",
    "in":   "25",
    "inc":  "26",
    "halt": "27"
}

REGISTERS = {
    "A": "0", "B": "1", "C": "2", "D": "3",
    "E": "4", "F": "5", "G": "6", "H": "7",
    "I": "8", "J": "9",
}

class Compiler:
    def __init__(self):
        self.labels = {}

    def clean(self, code):
        out = []
        
        for line in code.splitlines():
            line = line.strip()
            if not line:
                continue

            # remove 3 comment styles
            if line.startswith("#") or line.startswith("//") or line.startswith(";"):
                continue

            # strip inline comments too
            for c in ["#", "//", ";"]:
                idx = line.find(c)
                if idx != -1:
                    line = line[:idx].strip()

            if not line:
                continue

            # enforce: first char must be alphanumeric
            if not line[0].isalnum():
                continue

            out.append(line)

        codelines = out.splitlines()
        while i < len(codelines):
            if codelines[i].contains("jmp", "jz", "jnz", "jg", "jl", "JMP", "JZ", "JNZ", "JG", "JL"):
                art = codelines[i].split()
                op = art[0]
                a = art[1]
                if not a in REGISTERS:
                    if a.isnumerical():
                        out.insert(i-1, f"MOVI J {a}")
                    else:
                        out.insert(i-1, "")

        return out

    def pass_labels(self, lines):
        pc = 0
        for line in lines:
            if line.endswith(":"):
                self.labels[line[:-1]] = pc
            else:
                pc += 1

    def expand(self, lines):
        pc = -1
        while pc<len(lines):
            pc += 1
            parts = line.split()
            op = parts[0]
            if op in ("jmp", "jz", "jnz", "jg", "jl", "JMP", "JZ", "JNZ", "JG", "JL"):
                a = parts[1]
                b = parts[2]
                # expand if lines are larger
                # replace the jmp w/ JMP J
                lines[pc+1] = f"{op} J"
                #  ins the movi BEFORE
                target = self.labels[a]
                lines[pc] = f"MOVI J {target + 1:02d}" 
                
    def encode(self, line):
        parts = line.split()
        
        op = parts[0]

        # jmp family blocks
        if op in ("jmp", "jz", "jnz", "jg", "jl", 
                  "JMP", "JZ", "JNZ", "JG", "JL"):
            if debug:
                print(f"Encoding: {line}")
            if self.labels.get(parts[1]) is None:
                if parts[1] in REGISTERS:
                    return OPCODES[op] + REGISTERS[parts[1]]
                else:
                    print("JMP Commands need a valid location, are you sure you A: are asking for a valid register, or B: have spelled the label correctly")
            else:
                target = self.labels[parts[1]]
                return OPCODES[op] + f"{target + 1:02d}"

        # 2 operand ops
        if op in ("add", "cmp", "mov", "sub", "mul", "div", "mod", "and", "or", "read", "store", "int", "in",
                  "ADD", "CMP", "MOV", "SUB", "MUL", "DIV", "MOD", "AND", "OR", "READ", "STORE", "INT", "IN"):
            if debug:
                print(f"Encoding: {line}")
            return (OPCODES[op] + REGISTERS[parts[1]] + REGISTERS[parts[2]])

        #because MOVI is special
        if op in ("movi", "MOVI"):
            if debug:
                print(f"Encoding: {line}")
            # return an actual number if the label doesn't exist, otherwise return the label's address, to allow for MOVI- CALL-
            if self.labels.get(parts[2]) is None:
                return OPCODES[op] + REGISTERS[parts[1]] + parts[2]
            else:
                target = self.labels[parts[2]]
                return OPCODES["jmp"] + f"{target + 1:02d}"

        # single operand ops
        if op in ("not", "inc", "push", "pop", "call", "NOT", "INC", "PUSH", "POP", "CALL"):
            if debug:
                print(f"Encoding: {line}")
            return OPCODES[op] + REGISTERS[parts[1]]
        
        #zero operand ops
        if op in ("nop", "halt", "ret", "NOP", "HALT", "RET"):
            if debug:
                print(f"Encoding: {line}")
            return OPCODES[op] + "00"

        if line.endswith(":"):
            return line
        return f"{line} LINE WASN'T ENCODED"

    def cull(self, line): 
        if line.endswith(":"):
            return "0000"
        return line

    def compile(self, code):
        lines = self.clean(code)
        self.pass_labels(lines)
        self.expand(lines)
        
        count = 0
        output = []
        for line in lines:
            count += 1
            cel = self.encode(line)
            if cel is None:
                print(f"Error encoding line {count} [INVALID POINTER]: '{line}'")
                break
            else:
                output.append(cel)

        count = 0
        runtime = []
        for line in output:
            count += 1
            runtime.append(self.cull(line))
    
        if cel is None:
            return ''
        return "\n".join(runtime)

code = """
; Executable Code in Assembly
; Run this program to see what returns (it should just be 1 line of 2700)

# The following code is commented out, except for HALT
# start:
# MOVI A 1 (store 1 in Register A)
# MOVI B 6 (store 2 in Register B)
# CMP A B (set the flags to (is A > B?), (is A == B?), (is A < B?), in the first loop, 1 < 6, so we get TFF, or 100 in binary)
# INC A (increment register A by 1, use ADD and MOVI for larger increments)
# JNZ start (IF: the flags (a>==<b) are NOT 0, ie: A>B || A<B, then Jump to: start)

HALT
"""

debug = False # SET TO FALSE BEFORE COMMITTING, this lists all processed commands, if you see an error, it prints the line that failed before the failure

# this is the exiter, processes everything
c = Compiler()
final = c.compile(code)
worked = True
count = 1
for m in final.splitlines():
    if not m.isnumeric():
        print(f"Error: \"{m}\" was not encoded properly, contains non-numeric characters. Line {count} (excluding comments and blank lines)")
        worked = False
    count += 1
if worked:
    print(final)    
