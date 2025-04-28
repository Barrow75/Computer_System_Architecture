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

# half-adder: Arithmetic circuit that adds two binary digits
# Sum = x'y + xy'
# Carry = xy

def sum(x,y):
    not_x = NOT(x) #x'
    not_y = NOT(y) #y'
    x_y = AND(not_x, y) # x'y
    xy_ = AND(x, not_y)
    S = OR(x_y, xy_)

    return S

def carry(x,y):
    C = AND(x,y)

    return C

print("x y | Sum Carry")
print("----------------")
for x in [0,1]:
    for y in [0,1]:
        S = sum(x, y)
        C = carry(x, y)
        print(f"{x} {y} | {S} {C}")