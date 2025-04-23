Manipulation of binary information is done by logic circuits called gates.
Gates are blocks of hardware that produce signals of binary 1 or 0 when input logic requirements are satified.

# AND Gate: 
- Logical multiplication of binary digits where 1 is called a high and 0 is called a low
- The output is 1 if the input A and B are both equal to 1
Algebraic Function of AND Gate:
  > x = AB <br>
  > x = A•B <br>
- In the CPU the AND gates are a major component to satisfy multiple occurances as true. They are used for arithmatic operations in logic units.
- In cybersecurity 
    - Firewalls
    - VPN Access
    - Secure System Logins
    - Secure Boot - The system checks if the bootloader is signed AND the firmware hash matches beofre proceeding

      
Truth Table: <br>
A  B  |  x  <br>
------------  <br>
0  0  |  0  <br>
0  1  |  0  <br>
1  0  |  0  <br>
1  1  |  1  <br>


# OR Gate:
- The OR gate produces the inclusive OR function that outputs 1 if the input A or input B or both inputs are 1
- Logical addition where if any input is 1 the output is 1
- If the input is low (0) then the output is low
Algebraic Function of OR Gate:
  > x = A + B <br>

- Alarm systems: If the sensor detects smoke, the OR gate creates a signal to trigger the alarm
- In Cybersecurity
    - Intrusion detection/Prevention System
- Control units to determine how to decode and execute instructions

Truth Table: <br>
A  B  |  x  <br>
------------  <br>
0  0  |  0  <br>
0  1  |  1  <br>
1  0  |  1  <br>
1  1  |  1  <br>


# Inverter/ NOT Gate:
- Has one input value and one output value
- Known as an inverting buffer
- Main point is to drive other gates that require a large amount of power
- Used for memory blocks in computers
- Also used to design RAM and registers used in processors

Truth Table: <br>
A |  x  <br>
------------  <br>
0 |  1  <br>
1 |  0  <br>

# Buffer 
- Used to amplify weak signals and  provide isolation between different parts of a circuit
- Used for timing delays in signal transmission
- RAM, CPU and peripherals communicating on a motherboard via shared data bus

  Truth Table: <br>
A |  x  <br>
------------  <br>
0 |  0  <br>
1 |  1  <br>

# NAND Gate
- The complement/inverse of the AND function
- NOT AND
- The universal gate that  all basic gates can be represented by
- Help detect if a single input to a digital system has gone low
- All logic circuits inside a CPU can be built from NAND gates

Truth Table: <br>
A  B  |  x  <br>
------------  <br>
0  0  |  1  <br>
0  1  |  1  <br>
1  0  |  1  <br>
1  1  |  0  <br>
