# boolean equations

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

# equation 1: F = x + y'z

def equation_1(x,y,z):
    y_not = NOT(y) # y'
    yz = AND(y_not, z) #y' * z
    F = OR(x, yz) # x + y'z
    return F

print("x y z | F")
print("-------------")

for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            F = equation_1(x,y,z)
            print(f"{x} {y} {z} | {F}")

print('\n')
# equation 2: F = x'y + yz' + yz + xy'z'

def equation_2(x,y,z):
    x_not = NOT(x) # x'
    y_not = NOT(y) # y'
    z_not = NOT(z) # z'
    xy = AND(x_not,y) #x'y
    yz_ = AND(y, z_not) #yz'
    yz = AND(y,z)  # yz
    xy_ = AND(x,y_not) # xy'
    xyz = AND(xy_, z_not) #xy'z'

    F1 = OR(xy, yz_)
    F2 = OR(F1, yz)
    F = OR(F2, xyz)

    return F

print("x y z | F")
print("-------------")

for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            F = equation_2(x,y,z)
            print(f"{x} {y} {z} | {F}")