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
    if length > 1:    
        expont = length - 1
        if sign == 1:
            expont = length - 2 
        new_n  = float(n) / (10**(expont))
        one_point_n  = float(new_n)
    else:
        one_point_n = float(n)
        expont      = 0

    return sign, one_point_n, expont #type int float int

def bias(true_exponent, op):
    if int(op) == 1:
        bias_exponent = true_exponent + 15 #half
    if int(op) == 2:
        bias_exponent = true_exponent + 127 #single
    if int(op) == 3:
        bias_exponent = true_exponent + 1023 #double
    
    return bias_exponent #type int

def mantissa(number, op):
    string   = str(number)
    temp     = string.split(".")
    manti_temp = temp[1]

    if int(op) == 1:
        mantissa =  manti_temp.ljust( 10,str(0))#half
    if int(op) == 2:
        mantissa =  manti_temp.ljust( 23,str(0))#single
    if int(op) == 3:
        mantissa =  manti_temp.ljust( 52,str(0))#double

    return mantissa #type string

def right_shift(n, exp_a, exp_b, op):
    diff = exp_a - exp_b
    if diff < 0:
        diff = diff * (-1)
    r_shift_int = (n >> diff) #type int
    
    manti_temp = bin(r_shift_int) #type string
    manti_temp = manti_temp.replace("0b","")

    if int(op) == 1:
        mantissa =  manti_temp.rjust( 10,str(0))#half
    if int(op) == 2:
        mantissa =  manti_temp.rjust( 23,str(0))#single
    if int(op) == 3:
        mantissa =  manti_temp.rjust( 52,str(0))#double

    #print(mantissa)
    #temp1 = mantissa[0 : len(mantissa) - diff ] 
    #temp2 = mantissa[len(mantissa) - diff : ]
    #r_shift_bin = temp2 + temp1
    #r_shift_bin = r_shift_bin.replace("0b","")
    r_shift_bin = mantissa

    return r_shift_int, r_shift_bin

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

    return mantissa #type string

sign_a, a, exp_a = one_point_format(in_a)
sign_b, b, exp_b = one_point_format(in_b)

bias_a = bias(exp_a, op)
bias_b = bias(exp_b, op)

mantissa_a = mantissa(a, op)
mantissa_b = mantissa(b, op)

decimal_value_a = binaryToDecimal(int(mantissa_a))
decimal_value_b = binaryToDecimal(int(mantissa_b))

r_mantissa_a, r_mantissa_a_bin = right_shift(decimal_value_a, exp_a, exp_b, op)
r_mantissa_b, r_mantissa_b_bin = right_shift(decimal_value_b, exp_a, exp_b, op)

expanded_man_a = expand_mantissa(r_mantissa_a, op)
expanded_man_b = expand_mantissa(r_mantissa_b, op)

print("Bias: " + str(bias_a) + " , " + str(bias_b))
print("Mantissa: " + mantissa_a + " , " + mantissa_b)
print("Decimal Mantissa: " + str(decimal_value_a) + " , " + str(decimal_value_b))
print("Decimal R_Mantissa: " + str(r_mantissa_a) + " , " + str(r_mantissa_b))
print("R_Mantissa: " + str(r_mantissa_a_bin) + " , " + str(r_mantissa_b_bin))

def two_complement(n,op):

    print('\n')    
    if int(op) == 1:
        length = 10
    if int(op) == 2:
        length = 23
    if int(op) == 3:
        length = 52
    #string = str('{0:')  + str('b}') #+ str('{}'.format(length))
    print('number: ',str(n) + str("  Len: ")+ str(len(str(n))))
    
    binary = int(str(n))
    print('int number: ',str(binary) + str("  Len: ")+ str(len(str(binary))))
    
    int_ones_complement = ~ binary
    print('complement: ',str(int_ones_complement) + str("  Len: ")+ str(len(str(int_ones_complement))))

#    twos_b = str('1') + twos_b.replace("-","")

    #str_add_ones        =  str(int_ones_complement).rjust( length,str(1))
    #str_add_ones        =  str(int(int_ones_complement) + 1)
    #print('append 1: ',str_add_ones + str("  Len: ")+ str(len(str_add_ones)))

    z = int(int_ones_complement) + 1
    print('z= ',z)
    print('l(z)', len(str(z)))

#    int_twos_complement = int(str('-') + str_add_ones.replace("-","")) + 1
    int_twos_complement = int(int_ones_complement) + 1
    int_ones_complement = str(int_ones_complement).replace("-","")
    str_add_ones        =  int_ones_complement.rjust(length,str(1))
    
    str_twos_complement = str(str_add_ones) #.zfill(length+1)    
    print(str(str_twos_complement) + str("  Len: ")+ str(len(str_twos_complement)))

    print('\n')

    return str_twos_complement

# if math.trunc(float(in_a)) < 0:
#     twos_a = two_complement(r_mantissa_a, op)
#     twos_a = str('1') + twos_a.replace("-","")
#     print(twos_a)
# else:
#     pass
# if math.trunc(float(in_b)) < 0:
#     twos_b = two_complement(r_mantissa_b, op)
#     twos_b = str('1') + twos_b.replace("-","")
#     print(twos_b)
# else:
#     pass
print("Mantissa: ",r_mantissa_a_bin)
print(len(r_mantissa_a_bin))
x = two_complement(int(mantissa_b), 2)
print('---------',int(mantissa_b))
print(int("{b}".format(int(mantissa_b))))
print("HERE,",x)
#print(int(r_mantissa_a) + int(r_mantissa_b) )
#print(x)
#print(int(x))
#print(bin(int(x)))



