# Half Adder:
  - The  most basic digital arithmetic circuit is the addition of two binary digits (two bits)
  - Input variables of a half adder are called the augend and addend bits
  - The output output variables the sum and carry
  - Necessary to specify two output variables because the sum of 1 + 1 = 10
      - Symbols x and y to the input variables
      - S (sum) and C (carry) to the output variables
      - C output is 0 unless both inputs are 1
   
  - Equations: <br>
      S = x'y + xy' = x ⊕ y (XOR) <br>
      C = xy 

# Full Adder:
  - Combinational circuit that forms the arithmetic sum of three input bits
  - Three inputs and two outputs
  - Two inputs dentoed by x and y
  - Third input represents the carry from the previous lower significant position
  - S output is equal to 1 when only one input is equal to 1 or when all three inputs are equal to 1
  - C output carries 1 if two or three inputs are equal to 1

    - Equations: <br>
        S = x ⊕ y ⊕ z <br>
        C = xy + (x ⊕ y)z
