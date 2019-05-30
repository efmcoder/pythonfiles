#Write a function called f_to_c that takes an input f_temp, a temperature in Fahrenheit, and converts it to c_temp, that temperature in Celsius.
#It should then return c_temp.

def f_to_c(f_temp):
    return (f_temp - 32) * 5/9

print(f_to_c(82))
print(f_to_c(32))
print(f_to_c(100))

#Let’s test your function with a value of 100 Fahrenheit.
#Define a variable f100_in_celsius and set it equal to the value of f_to_c with 100 as an input.

f100_in_celsius = f_to_c(100)

#CONVERT Fahrenheit to Celsius
#Write a function called c_to_f that takes an input c_temp, a temperature in Celsius, and converts it to f_temp, that temperature in Fahrenheit.
#It should then return f_temp.
#The equation you should use is:
#Temp (F) = Temp (C) * (9/5) + 32

def c_to_f(c_temp):
    return (c_temp * 9/5) + 32
print(c_to_f(82))
print(c_to_f(32))
print(c_to_f(100))

#Let’s test your function with a value of 0 Celsius.
#Define a variable c0_in_fahrenheit and set it equal to the value of c_to_f with 0 as an input.

c0_in_fahrenheit = c_to_f(10)
print(c0_in_fahrenheit)

#Define a function called get_force that takes in mass and acceleration.
#It should return mass multiplied by acceleration.
#Print the string “The GE train supplies X Newtons of force.”, with X replaced by train_force.

def get_force(mass, acceleration):
    return mass * acceleration

#train_force = get_force(train_mass, train_acceleration)
train_force = get_force(1000,40)
print("The GE train supplies " + str(train_force)+" Newtons of force.")


#Define a function called get_energy that takes in mass and c.
#c is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. Set c to have a default value of 3*10**8.
#get_energy should return mass multiplied by c squared.

def get_energy(mass, c=3*10**8):
    return mass * c**2
#print(get_energy(1))

#Test get_energy by using it on bomb_mass, with the default value of c.
#Save the result to a variable called bomb_energy.
#Print the string “A 1kg bomb supplies X Joules.”, with X replaced by bomb_energy.
bomb_energy = get_energy(1)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")


#Define a final function called get_work that takes in mass, acceleration, and distance.
#Work is defined as force multiplied by distance.
#First, get the force using get_force, then multiply that by distance. Return the result.

def get_work(mass, acceleration,distance):
    force = get_force(mass, acceleration)
    return force * distance

#train_work = get_work(train_mass, train_acceleration, train_distance)
#train_work = get_work(1000, 40, 1)
#print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
print("The GE train does " + str(20000) + " Joules of work over " + str(100) + " meters.")
