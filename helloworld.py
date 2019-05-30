print("Hello, World!")


#Functions in python always start with the word "def"
def sing():
    print("you may say I'm a dreamer \nbut I'm not the only one \nI hope some day you'll join us \nand the world will live as one")

sing()
#call the function sing. Note there are no colons or semicolons

def loading_screen():
    print("This page is loading...")
    print("This will print because it's indented with above line")
print("This will not print because it's not indented")

loading_screen()

def mult_two_add_three(number):
    #number = 5
    print(number*2 + 3)

mult_two_add_three(5)

def greet(store, special):
    print("Welcome to " + store + ". " "\nOur special is " + special + ". " "\nHave fun shopping")


greet("Shaws", "tomatoes")
greet(store="Stop n Shop", special="avocadoes") #keyword arguments

def create_spreadsheet(title, rows):
    print("Creating a spreadsheet titled " + title + " with " + rows + " rows")
create_spreadsheet("P&L", "1000")


def divide_by_four(number):
    return number/4

result = divide_by_four(16) #must not be indented
print(divide_by_four(16))
print("16 divided by 4 is " + str(result) )


#mutliple parameters
def calculate_age(this_year, birth_year):
    age = this_year - birth_year
    return age

my_age = calculate_age(2049, 1993)
dads_age = calculate_age(2049, 1953)
print("I am " + str(my_age) + " years old and my dad is " + str(dads_age) + " years old")
print(str(my_age) + ", " + str(dads_age))


#return multiple values
def square_point(x_value, y_value):
    x_2 = x_value * x_value
    y_2 = y_value * y_value
    return x_2, y_2

print(square_point(2,3))



def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = target + margin
  return low_limit, high_limit

low, high = get_boundaries(100, 20)

#we added this print statement just to sanity-check our solution:
print("Low limit: "+str(low)+", high limit: "+str(high))


#scope
#def create_special_string(special_item):
#    return "Our special is " + special_item + "."

#print("I don't like " + special_item) #out of scope coz special item is defined above INSIDE the space of a funcction and not outside


current_year = 2048

def calculate_age(birth_year):
  age = current_year - birth_year
  return age

print(current_year)

print(calculate_age(1970))

#FINAL
def repeat_stuff(stuff, num_repeats=10):
  return stuff*num_repeats

lyrics = repeat_stuff("Row ", 3) + "Your Boat. "
song = repeat_stuff(lyrics)

print(song)
