# build logic gates

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

# D Flip Flop
# one input

# initial state
Q = 0
prev_clk = 0

def D_Flip_Flop(D, clk):
    global Q, prev_clk

    if prev_clk == 0 and clk == 1:
        Q = D

    prev_clk = clk
    return Q

testing = [
    (0, 0),
    (0, 1),
    (1, 0),
    (1, 1),
    (0, 0),
    (0, 1)
]
print("D CLK | Q")
print("-------------")
for D,clk in testing:
    output = D_Flip_Flop(D, clk)
    print(f"{D}  {clk}  | {output}")