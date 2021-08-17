#we gaan een function schrijven die hallo zegt tegen iemand
#alle code in deze function moet indeneted zijn
def zeg_hallo():
    print("Hallo wereld")


#code in een funciton waordt ppas uitgevoer dwanner we het callen

#flow van function
print("boven")
zeg_hallo()
print("onder")


#paramater is information die we passseren in een function
def zeg_hallo(name):
    print("Hallo " +  name)

zeg_hallo("Derik")

#ja kan meerder parameters passen, bijvoorbeel age

def zeg_hallo(name, age):
    print("Hallo " +  name  + " je bent" + age + "jaar oud")

zeg_hallo("Derik", "54")
zeg_hallo("Henk", "23")
