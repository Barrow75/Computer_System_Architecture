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
