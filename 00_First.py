#Variabelen in Python, Variables are containers for storing data values.
print("Deel 1: variabelen in Python")
z = 8 #integer
d = 8.6 #float
print(z)
print(d)

#Python has no command for declaring a variable.
a = "Hello"
b = "World" #String
c = a + " " + b
print(c)

print(type(a))
print(type(b))
print(type(c))

c = 8
print(type(c))
c = 8x
print(type(c))

print("______")
print("|    /|")
print("|   / |")
print("|  /  |")
print("|/____|")


"""
Working with strings
"""
txt = "We are the so-called \"Vikings\" from the north."
print(txt.upper())
print(txt.lower())
print(len(txt))

print(txt.islower())
print(txt.lower().islower())
#WE KUNNE OOK CHARACHTERS PAKKEN UIT EEN STRING
print(txt[3]) # string is indexed met 0
print(txt.index("W")) #index funciton vertelt ons waar een speccifieik incdex of Stinrg is located
# we geven heir een waarde aan index, dit noemen we passing a value, a paramter into a function
#gooi je een paramater di einiet in de sting voorkomt dan krijg je een error


print(txt.replace("Viking", "CheesKings"))





"""
#Draw a line in a diagram from position (0,0) to position (6,250):
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
"""
