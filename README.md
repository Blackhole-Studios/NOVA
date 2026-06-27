# NOVA
NOVA - New Operational Virtual Assembly. Nova is a Turbowarp based VM, not OS, but instead a virtual machine. HOWEVER, an OS could be created in the future on the NOVAKernel

<div align="center">

# 🌌 NOVA

### *A Virtual Computer Architecture Built Entirely in Scratch*

*A complete software computer featuring a custom CPU, instruction set, boot ROM, RAM, stack hardware, assembler, and operating system.*

---

![Status](https://img.shields.io/badge/Status-Active_Development-brightgreen)
![Language](https://img.shields.io/badge/Language-NOVASM-blue)
![Architecture](https://img.shields.io/badge/Architecture-16--bit-orange)
![Assembler](https://img.shields.io/badge/Assembler-Python-yellow)
![License](https://img.shields.io/badge/License-MIT-purple)
![Made In](https://img.shields.io/badge/Language-Turbowarp-maroon)

</div>

---

# What is NOVA?

**NOVA** is a complete virtual computer built from scratch inside **Scratch/TurboWarp**.
**NOVA** also stand for "New Operational Virtual Assembly" 

Rather than emulating an existing CPU, NOVA introduces an entirely original architecture featuring its own:

* CPU
* Assembly language
* Machine code format
* Boot ROM
* RAM controller
* Stack hardware
* Interrupt system
* Operating System

Every instruction executed by NOVA is interpreted by a CPU built entirely from Scratch blocks.

---

# Features

* Custom CPU architecture
* Original assembly language (**NOVASM**)
* Decimal machine code
* Virtual RAM
* Hardware stack
* Interrupt support
* Boot ROM
* Disk bootloader
* Blazing fast Python assembler
* External ROM loading
* Deterministic execution

---

# Architecture

```text
┌────────────────────────────────────────────────┐
│                  NOVA Motherboard Layout       │
│                                                │
│                                                │
│                                                │
│   ┌──┐bootROM                                  │
│┌──│  │                                         │
││  └──┘            ┌─────────────────┐          │
││  ┌──────┐        │────────────TIME │          │
││  │RAM   │        │┌──┐ ┌──────────┐│          │
│└──│128KB │        ││ST│ │Central   ││          │
│   │      │────────││AC│ │Processing││          │
│   │      │ Ram    ││K │ │Unit      ││          │
│   │      │ Bus    ││  │ │          ││          │
│   │      │────────│└──┘ └──────────┘│          │
│   │      │        │ ┌──────────────┐│          │
│   │      │        │ │REGISTERS (10)││────┐     │
│   │      │        │ └──────────────┘│    │     │
│   │      │        └─────────────────┘    │     │
│   │      │        ┌─────────────────┐    │     │
│   └──────┘┌───────│DEVICE I/O System│────┘     │
│     │     │       └─────────────────┘────┐     │
│     │     │   DEVICE        │    BUSSES  │     │
│     │     │                 │            │     │
│     │     │                 │            │     │
│  ┌─────────┐           ┌────────┐  ┌───────┐   │
│  │ HDD     │           │USB     │  │WI-FI  │   │
│  │ 8MB     │           │1MB     │  │       │   │
│  │         │           │        │  │       │   │
│  │         │           │        │  │       │   │
│  └─────────┘           └────────┘  └───────┘   │
└────────────────────────────────────────────────┘
```

---

# CPU

The NOVA CPU executes machine code directly from RAM.

Current capabilities include:

* Register operations [MOV, MOVI]
* Integer arithmetic [ADD, SUB, MUL, DIV]
* Memory access
* Conditional branching [JMP, JZ, CMP...]
* Procedure calls
* Interrupts [in Process]
* Stack manipulation [PUSH, POP, CALL, RET]
* Binary logic [AND, OR, NOT on decimals]
* Hardware I/O [HDD, USB, WIFI]
* HALT instruction

---

# NOVASM (NOVA - ASM)

Example program:

```asm
MOVI 1 53
MOVI 2 200
STORE 1 2

READ 2 3
CMP 1 3
JNZ 0

HALT
```

Compiled machine code:

```text
02153
022200
0412
0323
1213
180
27
```

---

# Instruction Set

Current instruction count:

| Category     | Instructions |
| ------------ | -----------: |
| Data         |            6 |
| Math         |            5 |
| Logic        |            4 |
| Flow Control |            5 |
| Stack        |            2 |
| System       |            4 |
| Extra        |            1 |

**Total:** **27 Instructions**

---

# Memory Model

NOVA separates hardware into independent components.

* CPU
* RAM
* Stack
* Boot ROM
* Disk [HDD & USB]
* I/O

Each behaves like its own hardware device and communicates over a simulated bus.

---

# Boot Process

```text
Power On
    │
    ▼
RAM initializes along with HDD/USB to prevent early overwrites
    │
    ▼
Boot ROM into sector 1 of RAM
    │
    ▼
CPU boots ROM by executing with Program Counter = 1
    │
    ▼
Searches all hardware devices for a bootloader
    │
    ▼
Grabs first bootloader (USB before HDD)
    │
    ▼
Search disk with bootloader for a bootable Kernel
    │
    ▼
Load Kernel into RAM
    │
    ▼
Jump to Kernel
```

---

# Repository Structure

Not all files are exact, esp Packages in the future, that won't be updated with each new package, it'll stay as is
```text
NOVA/
├── .github/
│   └── worflows
│       └── main.yml (Auto Pull Validator/rejector for packages)
│
├── Documentation/
│   ├── ISA.md
│   ├── Packages.md
│   └── instruction-set.txt 
│
├── Kernels/
│   ├── testKernel
│   └── #No kernel is currently programmed, but in the future, this is where it'll go, the one present is a placeholder
│
├── Packages/
│   ├── testpackage
│   ├── #Unused as of now, this will allow the kernel to install packages like Desktop Environemnts
│   └── #or maybe apps through a scratch attach server to this repository folder.
│
├── Programs/
│   ├── NOVA.html [Compiled turbowarp project]
│   └── Assembler.py
│
├── Projects/
│   ├── #More projects soon, like a scratch version of my ASSEMBLER along with an IDE?
│   └── NOVA.sb3 [a Turbowarp Project](https://turbowarp.org)
│
├── Work Files/
│   ├── ErrTrace.txt [previous execution call]
│   ├── boot.dimg [simple boot ROM program]
│   └── boot2.dimg [complex boot ROM program]
│
└── README.md
```

---

# Current Progress

* ✅ CPU
* ✅ Machine code decoder
* ✅ Instruction execution
* ✅ RAM hardware
* ✅ Stack hardware
* ✅ Boot ROM
* 🔄 Python assembler
* 🔄 HALT instruction
* 🔄 Bootloader
* 🔄 Kernel
* ⏳ File system
* ⏳ Shell
* ⏳ Device drivers

---

# Goals

* Complete operating system
* Executable applications
* File system
* Multi-program support
* Virtual disk images
* Developer tools
* Debugger
* Emulator improvements
* Community Generated Programs

---

# Design Philosophy

NOVA is designed to be:

* Simple enough to understand
* Powerful enough to write an operating system
* Built from FIRST principles
* Educational
* Fun to hack on

Rather than copying x86 or ARM, NOVA is its own architecture with its own design decisions, which allows it to run in [Turbowarp](https://turbowarp.org) (an accelerated modified version of [Scratch](https://scratch.mit.edu))

---

# Contributing

Contributions, bug reports, feature ideas, and pull requests are welcome.

If you discover a bug in the CPU, assembler, or operating system, feel free to open an issue.

As well, NOVA wouldn't be impressive unless a community helps to program on the platform, so exterior contributions are welcome and can be pulled into /packages as well as under their working OS.
And other types of programs for the overall ease of programming (like IDE's or Servers) are welcomed into /programs happily if they are quality.

---

# **License**

This project is licensed under the MIT License.

---

<div align="center">

## 🌌 NOVA

**"Simplicity is the prerequisite to Reliability" - Edgar Djikstra**

Made with ❤️ in Scratch and Turbowarp.

</div>
