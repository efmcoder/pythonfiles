#Write a function called f_to_c that takes an input f_temp, a temperature in Fahrenheit, and converts it to c_temp, that temperature in Celsius.
#It should then return c_temp.

def f_to_c(f_temp):
    return (f_temp - 32) * 5/9

print(f_to_c(82))
