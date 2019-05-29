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

def mult_two_add_three():
    number = 5
    print(number*2 + 3)

mult_two_add_three();
