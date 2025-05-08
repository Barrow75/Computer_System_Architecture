# What are Flip Flops:
  A binary cell capable of storing one bit of information. 
  It has two outputs: <br>
       One for the normal value and one for the complement value of thhe bit stored in it <br>

  A flip flop maintains a binary state until directed by a clock pulse to switch states

  The difference among differet types of flip flops is the number of inputs they possess an in the manner in which the inputs affect the binary state

# SR Flip Flop
- Set Reset flip flop is the simplest type of memory element
- Stores 1 bit either a 0 or 1
- Two Inputs: <br>
      > S = Set: tres to make the output 1 <br>
      > R = Reset: tries to make the output 0 <br>

- Two outputs: <br>
      > Q = main output <br>
      > Q' = inverted output <br>
    
- SR Flip Flop only reacts when the clk = 1
- The output changes only at the moment the clock tells it to. This prevents random updates and ensures synchronized
changes in multi bit circuits
- Simplest possible memory circuit in digital electronics.
- Fundamental idea of storing state ( remembering a bit over time)

# D Flip Flop
- Stores 1 bit either a 0 or 1
- Whatever value is on D at the moment of a clock tick is saved and held as the output Q
- Used in Registers, RAM cells, Buffers
- Helps in synchronized digital systems, avoiding glitches
- Allows circuits to remember past events or keep track of states
- Two inputs: <br>
      > D input: What to store <br>
      > Clock Input: When to store it 
- One Output: <br>
      > Q output: Stored value that doesnt change until next clock


# JK Flip Flop
- A type of flip flop that stores 1 bit and eiminates the invalid state found in the SR flip flop
- Three Inputs: <br>
      > J = Set input (S in the SR Flip Flip) <br>
      > K = Reset input (R in the SR flip flop) <br>
      > clk = clock input

- One output: <br>
      > Q = output (stored bit)

- Solves the SR flip flop problem; since in an SR flip flop if R = 1 and R = 1 is invalid the JK flip flop
replaces the invalid state
- Used in binary counters, digital clocks, timers
- Why use an SR over a JK: <br>
      - SR is simpler, faster and cheaper <br>
      - Good enough for simple circuits <br>
      - SR flip flops are like basic on and off switches <br>
      - JK flip flops are like smart switches but smart switches cost more and may not be needed for every lamp
  
