# NOVASM Instruction Set

## Registers

The CPU contains 10 general-purpose registers:

`A B C D E f g h i j`

Flags:

`Z` (Zero), `G` (Greater), `L` (Less)

The CPU can only read and write entire registers.

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
|     07 | `ADD A B`   | `A = A + B`                    |
|     08 | `SUB A B`   | `A = A - B`                    |
|     09 | `MUL A B`   | `A = A × B`                    |
|     10 | `DIV A B`   | `A = A ÷ B` (integer division) |
|     11 | `MOD A B`   | `A = A % B`                    |

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
|     17 | `JZ A`      | Jump if `Z` flag is set.         |
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
