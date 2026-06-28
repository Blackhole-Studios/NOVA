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

        return out

    def pass_labels(self, lines):
        pc = 0
        for line in lines:
            if line.endswith(":"):
                self.labels[line[:-1]] = pc
            else:
                pc += 1

    def encode(self, line):
        parts = line.split()

        op = parts[0]

        # jmp loop
        if op in ("jmp", "jz", "jnz", "jg", "jl", 
                  "JMP", "JZ", "JNZ", "JG", "JL"):
            if debug:
                print(f"Encoding: {line}")
            if self.labels.get(parts[1]) is None:
                if parts[1] in REGISTERS:
                    return OPCODES[op] + REGISTERS[parts[1]]
            else:
                target = self.labels[parts[1]]
                return OPCODES["jmp"] + f"{target + 1:02d}"

        # 2 operand ops
        if op in ("add", "cmp", "mov", "sub", "mul", "div", "mod", "and", "or", "read", "store", "int", "in",
                  "ADD", "CMP", "MOV", "SUB", "MUL", "DIV", "MOD", "AND", "OR", "READ", "STORE", "INT", "IN"):
            if debug:
                print(f"Encoding: {line}")
            return (
                OPCODES[op] + REGISTERS[parts[1]] + REGISTERS[parts[2]]
            )

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
; NOVA CPU VALIDATION TEST

; ---- Register setup (don't use more than 5 just in case) ----

MOVI A 5
MOVI B 10
MOVI C 15
MOVI D 20
MOVI E 25

; ---- Memory Load test W/ Register ABCDEF ----

MOVI F 100
STORE A F
MOVI F 101
STORE B F
MOVI F 102
STORE C F
MOVI F 103
STORE D F
MOVI F 104
STORE E F

; ---- Memory read test  W/ Register EFGHIJ----

MOVI E 100
READ E F
MOVI E 101
READ E G
MOVI E 102
READ E H
MOVI E 103
READ E I
MOVI E 104
READ E J

; ---- MOV ----

MOV A J
MOV J A

; ---- Arithmetic ----

ADD A B
SUB C B
MUL D B
DIV E B
MOD F G

; ---- Stack ----

PUSH A
PUSH B
PUSH C
PUSH D

POP D
POP C
POP B
POP A
; nothing should be changed in the registers if the stack is working properly

; ---- CALL TEST ----

MOVI F subroutine
CALL F

; ---- Loop ----

MOVI E 0
MOVI F 10

loop:
INC E
CMP E F
JL G

; ---- Greater Than ----

CMP F E
JG J

; ---- Equal ----

CMP E F
JZ I

HALT

; SUBROUTINE

subroutine:
INC A
INC B
RET
"""

debug = False # SET TO FALSE BEFORE COMMITTING (works fine just ugly output)

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