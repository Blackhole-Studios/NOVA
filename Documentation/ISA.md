# NOVASM Instruction Set

## Registers

The CPU contains 10 general-purpose registers:

`A B C D E F G H I J`
This is how both Compilers store them, and the Register's real names, However:
in the runtime env, it's `1 2 3 4 5 6 7 8 9 10`, the Compiler simply maps them and subtracts 1 (because 10 cannot be passed in as a valid register, 1 is added once processed)

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
This above code withh repeat the indented sectior 4 times (one on initital, the ``JL 3`` repeated 3 times, a base REPEAT (X) loop)

As well, the Compiler works much better, this is valid code to do the same thing:
```code
MOVI A 0
MOVI B 4
MOVI D 1
loop:
ADD A D
CMP A B
JL loop
# Following code
```
This above script is a FOR loop, here's a WHILE loop:
```code
MOVI A 0
MOVI B 5
MOVI C 1
loop:
CMP A B

JG end
; Code goes here
; compuation +_+
ADD A C
JMP loop

end:
```

Obviously an infinite loop, don't use, unless like for the Kernel, a script that SHOULD NOT END
```code
loop:

;code +_+

JMP loop
```

In the following versions, we will hopefully have compacted 'ifs' supported/in the compiler, IE: this should be valid code:
```code
MOVI A 0
MOVI B 4
MOVI D 1
loop:
ADD A D
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

1. **CMP:** Sets flags to `100` (`A>B`), `010` (`A=B`), or `001` (`A<B`).

2. **Bitwise Operations:** `AND`, `OR`, and `NOT` operate on the binary representation of the register values.

3. **INT:** Equivalent to saving the current execution context (`PC`, flags, and registers) before jumping to the interrupt handler.

4. **IN:** Interfaces with hardware devices (disk, keyboard, timer, etc.). No standard devices are currently implemented.
