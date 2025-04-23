# simple Logic Gates

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


print("A B | AND OR NAND NOR XOR XNOR")
for A in [0, 1]:
    for B in [0, 1]:
        print(f"{A} {B} |  {AND(A, B)}   {OR(A, B)}   {NAND(A, B)}   {NOR(A,B)}    {XOR(A,B)}    {XNOR(A,B)} ")