# wegaan een funtcion maken die 3 paramaetres als input neemt
# if met comparison operators

def max_num(num1, num2 , num3):
    if num1 >= num2 and num1 >= num3:
        return num1
#we krijgen hier ene boleanse waarde als antwoord, maar gebruiken comparison operators
    elif num2 >= num1  and  num2  >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))
