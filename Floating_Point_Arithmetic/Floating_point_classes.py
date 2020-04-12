import math

#in_a = input("\nBinary number 1: ")
#in_b = input("Binary number 2: ")
#op = input("\nHalf Precision: 1\nSingle Precision: 2\nDouble Precision: 3\n")
in_a = 100101.1
in_b = -1001110.01
op   = 2
#print ('\nin_a = ',in_a)
#print ('in_b = '  ,in_b)
#print ('in_op = ' ,op)
print('\n')

def one_point_format(n):
    sign = 0
    if math.trunc(float(n)) < 0:
        sign = 1
    string = str(n)
    temp   = string.split(".")
    length = len(temp[0])
    expont = length - 1
    if sign == 1:
        expont = length - 2 
    new_n  = float(n) / (10**(expont))
    new_n  = float(new_n)

    return sign, new_n, expont

def bias(true_exponent, op):
    if int(op) == 1:
        bias_exponent = true_exponent + 15 #half
    if int(op) == 2:
        bias_exponent = true_exponent + 127 #single
    if int(op) == 3:
        bias_exponent = true_exponent + 1023 #double
    
    return bias_exponent

def mantissa(number, op):
    string   = str(number)
    temp     = string.split(".")
    manti_temp = temp[1]
    #manti_temp = string
    #manti_temp = bin_n.replace("0b","")#   bin(n).replace("0b","")
    if int(op) == 1:
        mantissa =  manti_temp.ljust( 10,str(0))#half
    if int(op) == 2:
        mantissa =  manti_temp.ljust( 23,str(0))#single
    if int(op) == 3:
        mantissa =  manti_temp.ljust( 52,str(0))#double

    return mantissa

def right_shift(n, exp_a, exp_b, op):

    diff = exp_a - exp_b
    if diff < 0:
        diff = diff * (-1)
    #shifted = "1" + str(n)
    r_shifted = (n >> diff)
    manti_temp = bin(r_shifted)
    manti_temp = manti_temp.replace("0b","")

    if int(op) == 1:
        mantissa =  manti_temp.ljust( 10,str(0))#half
    if int(op) == 2:
        mantissa =  manti_temp.ljust( 23,str(0))#single
    if int(op) == 3:
        mantissa =  manti_temp.ljust( 52,str(0))#double

    input = mantissa
    d = diff
    Rfirst = input[0 : len(input)-d] 
    Rsecond = input[len(input)-d : ]
    res = Rsecond + Rfirst
    res = res.replace("0b","")

    return r_shifted, res

def binaryToDecimal(n): 
    num = n; 
    dec_value = 0;  
    base = 1; 
    temp = num; 
    while(temp): 
        last_digit = temp % 10; 
        temp = int(temp / 10); 
        dec_value += last_digit * base; 
        base = base * 2; 
    return dec_value;

def expand_mantissa(n, op):
    bin_n = bin(n)
    manti_temp = bin_n.replace("0b","")#   bin(n).replace("0b","")
    if int(op) == 1:
        mantissa =  manti_temp.ljust( 10,str(0))#half
    if int(op) == 2:
        mantissa =  manti_temp.ljust( 23,str(0))#single
    if int(op) == 3:
        mantissa =  manti_temp.ljust( 52,str(0))#double

    return mantissa

#sign, number , exponent = one_point_format(-111.0101)
sign_a, a, exp_a = one_point_format(in_a)
sign_b, b, exp_b = one_point_format(in_b)

bias_a = bias(exp_a, op)
bias_b = bias(exp_b, op)

mantissa_a = mantissa(a, op)
mantissa_b = mantissa(b, op)

decimal_value_a = binaryToDecimal(int(mantissa_a))
decimal_value_b = binaryToDecimal(int(mantissa_b))

new_man_a, one = right_shift(decimal_value_a, exp_a, exp_b, op)
new_man_b, two = right_shift(decimal_value_b, exp_a, exp_b, op)

expanded = expand_mantissa(new_man_a, op)

print("Bias: " + str(bias_a) + " , " + str(bias_b))
print(type(bias_a))
print(type(bias_b))
print("Mantissa: " + mantissa_a + " , " + mantissa_b)
print(type(mantissa_a))
print(type(mantissa_a))
print("now ",decimal_value_a)
print("now ",decimal_value_b) 
print(new_man_a)
print(new_man_b)
print("Yo, ",type(bin(new_man_a)))
print("-------",one)
print("-------",two)
print(bin(new_man_a))
print(bin(new_man_b)) 
print(expanded)






