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

# full-adder: Arithmetic circuit that adds 3 binary digits
# Sum = x ⊕ y ⊕ z
# Carry = xy + (x ⊕ y)z

def sum_bits(x,y, z):
    S1  = XOR(x, y)
    S = XOR(S1, z)

    return S

def carry(x,y, z):
    C1 = AND(x,y)
    C2 = XOR(x,y)
    C3 = AND(C2, z)
    C = OR(C1, C3)

    return C

print("x y z | C S")
print("----------------")
for x in [0,1]:
    for y in [0,1]:
        for z in [0, 1]:
            S = sum_bits(x, y, z)
            C = carry(x, y, z)
            print(f"{x} {y} {z} | {C} {S}")