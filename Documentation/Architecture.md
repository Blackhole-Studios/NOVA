# The Architecture of NOVA
### The architecture of a Virtual Computer is VERY important
There's a rough diagram in ASCII made in ASCII ART STUDIO, but for text based readers, I'll describe it here too.

## CPU
The CPU computes 4 steps per 'cycle', on moderate hardware (My PC, an i7-4790k w/ 16gb DDR3) it should complete around 3000 cycles a second in Turbowarp (THANK YOU GARBOMUFFIN FOR OPTIMIZATION)
The CPU is About your cpu's GHZ but in KHZ, for example, my CPU is 3.3 GHZ, so my simulation runs at 3.3 KHZ, my laptop @ 1.6 KHZ does quite worse at about 1.2KHZ, but in that range.

> EDIT: ignore that above statistic, I ran another benchmark, and got an eyewatering 20KHZ, this works by turning OFF the compiler, as if not, it caps at 3k executed lines

The CPU Executes 4 steps per cycle:
1.  Increment Program Counter by 1
2.   Pull the Executed line from RAM (if Program Counter is say, 32, we execute cell 32 in ram as a command. A common source of errors is the CPU 'jailbreaking' and running into data rather than straight machine code) 
3.   Parse the Line
4.   1.  Execute the Line
     2.  Check OP Code with THE IF
     3.  Execute the OPIF if applicable (ie: the `CMP` command runs an IF statement inside of it's executing area, which makes it slower than other)
     4.  Store the result/do the modify (ie: the `ADD` command needs to Write to a register)

The Hardware for the CPU is a set 10 registers, each only holding a reccomended 8 digibits (12345678 for example). I say reccomended as technichally they could hold 256 digitbits, but if you write the register to ram with > 8 bits, it truncates it down, losing infomation.

## RAM
RAM, or Random Access Memory (Not to be confused with the Hit album by French band 'Daft Punk', Random Access Memor[ies]), is the CPU's larger storage than it's limited cache size of 80 digits.
The typical RAM Init size is about 50 Kilobytes, which is quite large for such a simulation. As a package developer, this wouldn't affect you, the ram size should matter to Kernel Devs.

RAM is built from cells, which are items of a very large scratch list (each one is inited with '00000000' or 8 zeros)

A typical Ram usage Would be as follows:
```code
READ A B
# Meaning: Read register A's address in RAM to register B

FIRST:
CPU initiates a call to the RAM in THE IF
CPU's RAM MANAGER handles it, and waits until the RAM BUS is open (if taken up by say the HDD)
Once open, the RAM MANAGER copies the following data into the RAM BUS:
RB[1] = SIGNAL (used for just making sure no 2 devices try to write to the RAM BUS at the same time)
RB[2] = BusReady (used by the RAM system to mark whether RAM is open to actions, ie: if processing a HDD request)
RB[3] = 0 (0 signifies READ globally, from the setting device wanting to 'READ' the ram)
RB[4] = (Nothing, [4] is the DATA Channel, and a read doesn't require a DATA value)
RB[5] = Register A ([5] is the RAM Address, which is the ID of the CELL the ram manager should read from)
RB[6] = Public Gate (Very similar to [2])

Once the RAM System acknowledges the Read Request (by setting Bus Ready to FALSE)
it reads RB[3] to check if READ or WRITE, in this case, READ, so it sets RB[4] to RAM_CELL[5], before unlocking all the OUT gates, RB[6] for the CPU to then set Register B to RB[4]
```

## Devices
Devices are a work in progress, but they fall into 2 main catagories, CORE and USER, core devices come with the NOVA.html, USER devices can be added with the +SPRITE in the Turbowarp Editor w/ the NOVA.sb3
There is a set limit to the ammount of devices that can be apart of the CORE, being at max 9 devices, these get priority data transfer, all USER devices take slightly longer to send/recive data.

The command to access the devices is `IN`, so a way to access a device is `IN [PORT (from register) ] [DATA (from register (the only case when a register length can be > 8, because sometimes data is neccessary))]`

### The Devices as of now are as follows (Ports) :
1. HDD (for main Bulk storage) (>2MB)
2. USB (for booting ISOs/Kernels) (10KB)
3. Timer (for accessing time) (can be written to to update time for like time zone change)
4. WiFi Card (For connecting to the Scratch Attach Server, 2 versions, a Scratch that uses SA and Turbowarp that uses WH)
5. bootROM (can be used to see the ROM that booted the kernel, and can be written to) (like 100 Bytes, but modifiable)
6. GPU (Can write whole frames using the BUFFER (allocate the last like 1000 cells in RAM to the GPU), or do the hardcoded TXT Viewer that works by pushing text to the interface)
7. Keyboard (Cannot be written to, lists all characters pressed on kb, ie: Backspace, SHIFT, 'A', 'U' since the last POLL cycle (sums all keys pressed in the last 20ms))
8. Mouse (Lists current Mouse X and Y in a 2d state on the screen (0,0 (0 000 0 000)is centered, 1,1 (0 100, 0 100)is upper right, -1, -1 (1 100 1 100), it's in a ratio of /100s to the edge, so the screen is 200 divisions across, and 640px, therefore you get mouse resolution up to 2.3 pixels, which is smaller than it sounds))
9. This one isn't decided yet, maybe a seperate WIFI card? Maybe a Quantaum Chip?

10+ (All User Devices, custom uploads, don't use the same port for 2 devices, there are technically 99999999 ports, or ~2<sup>27</sup>)


### GPU
unfinished
### Wifi
unfinished
