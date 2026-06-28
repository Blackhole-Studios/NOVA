# NOVASM Instruction Set

## Registers

The CPU contains 10 general-purpose registers:

`A B C D E F G H I J`

Flags:

 `G` (Greater), `Z` (Zero), `L` (Less)

The CPU can only read and write entire registers.

---
## Loops

while in and of itself, the ISA does NOT support loops in an easy sense, they are totally possible, a valid script directly in ASM is:
```code
MOVI A 0
MOVI B 4
 NOP
 ADD A 1
 CMP A B
JL 3
# Following code
```
This above code withh repeat the indented sectior 4 times (one on initital, the ``JL 3`` repeated 3 times)

As well, the Compiler works much better, this is valid code to do the same thing:
```code
MOVI A 0
MOVI B 4
loop:
ADD A 1
CMP A B
JL loop
# Following code
```

In the following versions, we will hopefully have compacted 'ifs', IE: this should be valid code:
```code
MOVI A 0
MOVI B 4
loop:
ADD A 1
IF A < B: loop
# Following code
```
if you know my previous languages like [Amberscript](https://github.com/ItsGraphax/Amberscript), you'll see that I love one line IFs.

---

## DATA

| Opcode | Instruction    | Description                                  |
| -----: | -------------- | -------------------------------------------- |
|     01 | `MOV A B`      | Copy register `A` into register `B`.         |
|     02 | `MOVI A int`   | Load an immediate integer into register `A`. |
|     03 | `READ B A`     | Read RAM at address `B` into register `A`.        |
|     04 | `STORE A B`    | Store register `A` into RAM at address from register `B`.       |
|     05 | `PUSH A`       | Push register `A` onto the stack.            |
|     06 | `POP A`        | Pop the stack into register `A`.             |

## MATH

| Opcode | Instruction | Description                    |
| -----: | ----------- | ------------------------------ |
|     07 | `ADD A B`   | register `A = A + B`           |
|     08 | `SUB A B`   | register `A = A - B`           |
|     09 | `MUL A B`   | register `A = A × B`           |
|     10 | `DIV A B`   | register `A = A ÷ B` (integer division FLOOR) |
|     11 | `MOD A B`   | register  `A = A % B`             |

## LOGIC

| Opcode | Instruction | Description           |
| -----: | ----------- | --------------------- |
|     12 | `CMP A B`   | Compare `A` and `B`.¹ |
|     13 | `AND A B`   | Binary AND.²          |
|     14 | `OR A B`    | Binary OR.²           |
|     15 | `NOT A`     | Binary NOT.²          |

## FLOW

| Opcode | Instruction | Description                      |
| -----: | ----------- | -------------------------------- |
|     16 | `JMP A`     | Jump to address in register `A`. |
|     17 | `JZ A`      | Jump if `Z` flag is set to REG `A` |
|     18 | `JNZ A`     | Jump if `Z` flag is clear.       |
|     19 | `JG A`      | Jump if `G` flag is set.         |
|     20 | `JL A`      | Jump if `L` flag is set.         |

## STACK

| Opcode | Instruction | Description                  |
| -----: | ----------- | ---------------------------- |
|     21 | `CALL A`    | Push PC, then jump to `A`.   |
|     22 | `RET`       | Return from previous `CALL`. |

## SYSTEM

| Opcode | Instruction | Description                  |
| -----: | ----------- | ---------------------------- |
|     23 | `INT A`     | Trigger software interrupt.³ |
|     24 | `IRET`      | Return from interrupt.       |
|     25 | `IN port A` | Read from hardware device.⁴  |
|     26 | `INC A`     | Increment register `A` by 1. |
|     27 | `HALT`      | Stop execution.              |

---

### Notes

1. **CMP:** Sets flags to `100` (`A>B`), `010` (`A=B`), or `001` (`A<B`). Refer to **Flags**.

2. **Bitwise Operations:** `AND`, `OR`, and `NOT` operate on the binary representation of the register values. Refer to **Bitwise Operations**.

3. **INT:** Equivalent to saving the current execution context (`PC`, flags, and registers) before jumping to the interrupt handler. Refer to **Interrupts**.

4. **IN:** Interfaces with hardware devices (disk, keyboard, timer, etc.). No standard devices are currently implemented. Refer to **Device Bus Specification**.
