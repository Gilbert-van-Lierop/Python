def cube(num):
    num*num*num

cube(3)

#we gaan niets op het scherm krijgen, want cube doet niks
#al doen we
print(cube(3))
#dan krijgen we none op het scherm
#de oplossing heirvoor is rreturn sstatemtn, zodat de function iets terrgguggeft

def cube(num):
    return num*num*num


print(cube(3))

#ik kan een call ook in een variabele vast zetten
def cube1(num):
    return num*num*num
#    print("return stopt")

resultaat = cube1(10)

print(resultaat)
