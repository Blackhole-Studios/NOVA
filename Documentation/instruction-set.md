first is to discuss the Registers, the CPU can only read/write to full registers, there are 10 registers w/ names 'A', 'B', 'C', 'D', 'E', 'f', 'g', 'h', 'i', 'j' (lowercase == left, uppercase == right~~)
with flags Z, G, L
and RAM
ALL CPU instructions -- ASSEMBLY CODE -- NOVASM

DATA:
1. MOV A j (copies register A to register j, overwriting j in the process)
2. MOVI A int (forces the register to load a constant, good for writing)
3. READ addr A (loads ram @ address addr into register A)
4. STORE A addr (writes register A into ram @ address addr)
5. PUSH A (adds reg a to the stack) 
6. POP A (pulls the most recent stack to register A)

MATH:
7. ADD A B (adds register A to register B and stores it in register A)
8. SUB A B (substracts register B from register A and stores result in register A)
9. MUL A B (multiplies register A by register B and stores it in A)
10. DIV A B (divides register A by register B (truncated to 0 decimal places) and stores in A)
11. MOD A B (grabs remainder of register A by register B and stores in A )

LOGIC:
12. CMP A B (Compares register A and register B, if A > B: stores 100, if A=B, stores 010, if A<B stores 001)
13. AND A B (computes binary AND logical operator on registers A and B, through simulating binary values (eg: REGA = 1328 (0b10100110000) & REGB = 239(0b00011101111), REGA is set to the integer value for 0b00000100000 which is 32, meaning REGA = 32 after AND 1328 239))
14. OR A B (computes binary OR logical operator on registers A and B, through simulating binary values (eg: REGA = 1328 (0b10100110000) & REGB = 239(0b00011101111), REGA is set to the integer value for 0b10111111111 which is 1538 NOTE: THIS IS NOT AN ADD OPER))
15. NOT A (computes binary flip on register A (eg: RegA = 5, NOT A causes A to equal 2 because 5 in binary is 0b101, flipped (OR) is 0b010 or 2))

FLOW:
16. JMP A (sets PC (program counter, which stores the cell of executing) to register A)
17. JZ A (sets PC to register A IF and only IF flag Z is true, else continue)
18. JNZ A (sets PC to regiser A IFNOT and only IFNOT z is true (jumps if z=0))
19. JG A (sets PC to register A if G is true)
20. JL A (sets PC to register A if L is true)

STACK:
21. CALL A (adds current addr to the stack and jumps equal to: PUSH PC, JMP A)
22. RET (returns to last call equal to POP A, JMP A)

SYSTEM L:
23. INT A (interrupts the current program /the BREAKING NEWS command/ equal to: PUSH PC, PUSH flags, PUSH registers, PC = A)
24. IRET (returns from an interupt, it reloads the user register, the flags, and the pc and restarts control)
25. IN port A (read from a device into register, ie: timer, keyboard, mouse, disk) as of now: there are no valid ports suported
