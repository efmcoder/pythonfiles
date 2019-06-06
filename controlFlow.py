#first quick review
greeting = "Hello"
print("Hi")
print(greeting)
greeting = "Whatsapp?"
print(greeting)

#more variables with calculations
quilt_width = 8
quilt_length = 12
quilt_length = 8
print(quilt_width * quilt_length)

#functions
def repeat(stuff, num=10):
    return stuff*num
song = repeat("row ")
song2 = repeat("row ", 3) + "Your boat."
print(song)
print(song2)

def loading():
    print ("This page is loading")
loading()

def multiply(num):
    print(num*2 + 3)
multiply(5)

def many(num, x, y):
    print(num * x + y)
many(10,2,5)