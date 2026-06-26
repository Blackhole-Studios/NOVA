# NOVA
NOVA - New Operational Virtual Assembly. Nova is a Turbowarp based VM, not OS, but instead a virtual machine

# NOVA

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

</div>

---

# 🚀 What is NOVA?

**NOVA** is a complete virtual computer built from scratch inside **Scratch/TurboWarp**.

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

# ✨ Features

* 🧠 Custom CPU architecture
* 📜 Original assembly language (**NOVASM**)
* 🔢 Decimal machine code
* 💾 Virtual RAM
* 📦 Hardware stack
* ⚡ Interrupt support
* 🖥️ Boot ROM
* 💿 Disk bootloader
* 🔧 Python assembler
* 📁 External ROM loading
* 🎯 Deterministic execution

---

# 🏗 Architecture

```text
              +------------------+
              |     Boot ROM     |
              +--------+---------+
                       |
                       v
              +------------------+
              |       CPU        |
              +--------+---------+
                       |
        +--------------+--------------+
        |              |              |
        v              v              v
     Registers       Stack          I/O
        |                             |
        +--------------+--------------+
                       |
                       v
                    Virtual RAM
```

---

# 🧠 CPU

The NOVA CPU executes machine code directly from RAM.

Current capabilities include:

* Register operations
* Integer arithmetic
* Memory access
* Conditional branching
* Procedure calls
* Interrupts
* Stack manipulation
* Binary logic
* Hardware I/O
* HALT instruction

---

# 📖 NOVASM

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

# 🧩 Instruction Set

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

# 💾 Memory Model

NOVA separates hardware into independent components.

* CPU
* RAM
* Stack
* Boot ROM
* Disk
* I/O

Each behaves like its own hardware device and communicates over a simulated bus.

---

# ⚙ Boot Process

```text
Power On
    │
    ▼
Boot ROM
    │
    ▼
Load Bootloader
    │
    ▼
Search Boot Disk
    │
    ▼
Load Kernel into RAM
    │
    ▼
Jump to Kernel
```

---

# 📂 Repository Structure

```text
NOVA/
│
├── Assembler/
│   ├── ASMtoMAC.py
│   └── examples/
│
├── Scratch/
│   ├── CPU.sb3
│   ├── RAM.sb3
│   ├── Stack.sb3
│   └── BootROM.sb3
│
├── Kernel/
│
├── Documentation/
│
├── Programs/
│
└── README.md
```

---

# 🛠 Current Progress

* ✅ CPU
* ✅ Machine code decoder
* ✅ Instruction execution
* ✅ RAM hardware
* ✅ Stack hardware
* ✅ Boot ROM
* ✅ Python assembler
* ✅ HALT instruction
* 🔄 Bootloader
* 🔄 Kernel
* ⏳ File system
* ⏳ Shell
* ⏳ Device drivers

---

# 🎯 Goals

* Complete operating system
* Executable applications
* File system
* Multi-program support
* Virtual disk images
* Developer tools
* Debugger
* Emulator improvements

---

# 📊 Design Philosophy

NOVA is designed to be:

* Simple enough to understand
* Powerful enough to write an operating system
* Built from first principles
* Educational
* Fun to hack on

Rather than copying x86 or ARM, NOVA is its own architecture with its own design decisions.

---

# 🤝 Contributing

Contributions, bug reports, feature ideas, and pull requests are welcome.

If you discover a bug in the CPU, assembler, or operating system, feel free to open an issue.

---

# 📜 License

This project is licensed under the MIT License.

---

<div align="center">

## 🌌 NOVA

**"Because sometimes building the computer is more fun than using one."**

Made with ❤️ in Scratch.

</div>
