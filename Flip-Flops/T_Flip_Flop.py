# define the logic gates

# AND
def AND(A,B):
    x = A & B
    return x

# OR
def OR(A, B):
    x = A | B
    return x

# Inverter/ NOT
def NOT(A):
    x = ~A & 1
    return x

# Buffer
def Buffer(A):
    x = A & 1
    return x
# NAND
def NAND(A, B):
    x = NOT(AND(A, B))
    return x

# NOR
def NOR(A, B):
    x = NOT(OR(A, B))
    return x

# XOR
def XOR(A, B):
    x = A ^ B
    return x

# XNOR
def XNOR(A, B):
    x = NOT(XOR(A, B))
    return x



# Jk Flip FLop

# 2 inputs: J and K
# output: Q

# initial state
Q = 0
prev_clk = 0

def T_Flip_Flop(T, clk):
    global Q, prev_clk

    if prev_clk == 0 and clk == 1:
        if T == 0:
            pass
        elif T == 1:
            Q = ~Q & 1

    prev_clk = clk
    return Q

testing =[
    (0, 0),  # No edge
    (0, 1),  # T=0 → Hold
    (1, 0),  # Clock low
    (1, 1),  # T=1 → Toggle
    (1, 0),
    (1, 1),  # T=1 → Toggle again
    (0, 0),
    (0, 1),  # T=0 → Hold
    (1, 1),
    (1, 1),
    (0, 0),
    (1, 1)
]

print("T CLK | Q")
print("-------------")
for T, clk in testing:
    output = T_Flip_Flop(T, clk)
    print(f"{T}  {clk}  | {output}")