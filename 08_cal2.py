num1 =float(input("Vul het eerste nummer in: "))

operator = input("Geef de operator aan: ")

num2 =float(input("Vul het tweede nummer in: "))

#hoe weten we welke operator de gebruieker invoert?

if operator == "+":
    print("num1 en num2 =" ); print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    print("verkeerde operator ingevoerd")
