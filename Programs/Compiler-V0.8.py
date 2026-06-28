import re

# define opcode map
OPCODES = {
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
    "NOP":  "00",
    "HALT": "27"
}

def assemble_line(line):
    parts = line.strip().split()
    if not parts:
        return ""

    op = parts[0]
    opcode = OPCODES.get(op)

    if opcode is None:
        raise ValueError(f"Unknown opcode: {op}")

    # hlt
    if op == "HALT":
        return f"{opcode}"

    # MOVI (A IMM)
    if op == "MOVI":
        a = parts[1]
        imm = parts[2]
        return f"{opcode}{a}{imm}"

    # single register
    if op in ["INC", "POP", "PUSH", "NOT", "RET", "IRET", "NOP", "JMP", "JZ", "JNZ", "JG", "JL",]:
        if len(parts) == 2:
            return f"{opcode}{parts[1]}"
        return opcode + "0"

    # register-register
    if op in ["MOV", "ADD", "SUB", "MUL", "DIV", "MOD",
              "CMP", "AND", "OR", "READ", "STORE",
              "CALL", "INT", "IN"]:
        return f"{opcode}{parts[1]}{parts[2]}"

    raise ValueError(f"Bad format: {line}")

def assemble(program_text):
    output = []
    for line in program_text.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        output.append(assemble_line(line))
    return output


# example usage
if __name__ == "__main__":
    program = """
MOVI 1 0
MOVI 2 0
MOVI 3 999
MOVI 4 1
MOVI 5 50
MOVI 6 0
MOVI 7 0
MOVI 8 0
MOVI 9 0
MOVI 0 0

READ 2 6
CMP 6 0
JZ SAFE

MOVI 7 1
STORE 7 100
STORE 6 101
STORE 3 102
STORE 1 103
STORE 2 104
HALT

Safe:
JMP 20
    """

    machine = assemble(program)

    for m in machine:
        print(m)
