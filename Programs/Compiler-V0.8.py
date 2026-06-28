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
    NOP
    MOVI 3 9
    NOP
    INC 1
    CMP 1 3
    JG 19
    MOVI 2 1

    NOP
    NOP

    MOVI 3 0
    CMP 1 3
    JZ 17
    NOP
    HALT
    NOP
    JMP 4
    NOP
    HALT
    """

    machine = assemble(program)

    for m in machine:
        print(m)
