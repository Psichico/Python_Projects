#Also known as Q to Float

print('\n')
print("Enter Fixed Point Binary number:  ")

f = input()

whole, fraction = f.split('.')

temp = float(f) * (10**(len(fraction)))

print('\n')
print(f"Removed the Decimal point: {temp} \n")

#binary_f = bin(a)
binary_f = str(round(temp)) #To remove the decimal point in base 2 representation

decimal_f = int(binary_f,2)

answer = (decimal_f)/(2**(len(fraction)))

print(f"Fixed Point Decimal is : {answer}")
print('\n')