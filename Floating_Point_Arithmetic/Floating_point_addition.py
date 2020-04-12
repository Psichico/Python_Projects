# class user_input:

#     def __init__(self, number):
#         self.number = number
 
#     @classmethod
#     def take_input(num):
#         return num(
#                     int(input('Binary Input: ')),
#                     #int(input('Binary Input B: ')),
#                     )
import math

a = input("\nBinary number 1: ")
b = input("Binary number 2: ")

op = input("\nHalf Precision: 1\nSingle Precision: 2\nDouble Precision: 3\n")

print ('\na = ',a)
print ('b = ',b)
print ('op = ',op)

############### Sign Bit
if math.trunc(float(a)) >= 0:
    sign_bit_a = 0
else:
    sign_bit_a = 1

if math.trunc(float(b)) >= 0:
    sign_bit_b = 0
else:
    sign_bit_b = 1

print('\nsign_bit_a = ',sign_bit_a)
print('sign_bit_b = ',sign_bit_b)

###############

############### Biased Exponent
#assuming the number is given in points i.e. with a decimal point
string_a = str(a)
string_b = str(b)

tempa = string_a.split(".")
tempb = string_b.split(".")

len_a = len(tempa[1])
len_b = len(tempb[1])

true_a = len_a - 1
true_b = len_b - 1

if int(op) == 1:
    bias_a = true_a + 5
    bias_b = true_b + 5
    print("IN THE BIAS LOOP")
if int(op) == 2:
    bias_a = true_a + 127
    bias_b = true_b + 127
if int(op) == 3:
    bias_a = true_a + 1023
    bias_b = true_b + 1023

print ('Bias_a = ',bias_a)
print ('Bias_b = ',bias_b)
###############

############### Mantissa

m_a = tempa[1]
m_b = tempb[1]
print("mantissa a", m_a)
print("mantissa b", m_b)
###############

############### Compare Exponents and Right shift Mantissa
if bias_a > bias_b:
    bias_exp = bias_a
    m_a = int(str(1) + str(m_a))
    print("shifted a", m_a)
else:
    bias_exp = bias_b
    m_b = int(str(1) + str(m_b))
    print("shifted b", m_b)
###############

############### Two's complement
if sign_bit_a == 1:
    ones_comp = ~m_a
    temp = ones_comp + 1
    m_a = int(temp)
    print("-- ", m_a)
else:
    print('bits=',m_b)
    print(type(m_b))
    #m_b = "0b" + str(m_b)
    ones_comp = ~m_b
    print('ones ', ones_comp)
    temp = ones_comp + 1
    m_b = int(temp)
    print("++ ", m_b)


###############






