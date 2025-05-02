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



# SR Flip FLop

# 3 inputs: S (set) R(reset) C (clock)
# output: Q

# initial state
Q = 0
prev_clk = 0

def sr_Flip_Flop(S, R, clk):
    global Q, prev_clk

    if prev_clk == 0 and clk == 1:
        if S == 0 and R == 0:
            pass
        elif S == 0 and R == 1:
            Q = 0
        elif S == 1 and R == 0:
            Q = 1
        elif S == 1 and R == 1:
            print("Invalid")

    prev_clk = clk
    return Q

testing =[
    (0, 0, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 0 ,1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 1, 0),
    (1, 1, 1)
]

for S, R, clk in testing:
    output = sr_Flip_Flop(S, R, clk)
    print(f"{S} {R} {clk} | {output}")