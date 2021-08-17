#lists: ordered, mutable en allow duplicate elementes

friends = ["henk", "John", "Tessa"]

print(friends)
#acces elemetns based on their index
print(friends[0])

#elementen modiviceren
friends[1]= "Gina"
print(friends)

print(friends[-1])
#we kunnen ook een range slectere
print(friends[1:3])


#order de lists
lucky_numbers = [4,8,12,13,23,53]
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)


a = lucky_numbers[1:5]
print(a)
#als we geen start index zetten, start het vanaf het begin
#als we geen stop index zetten, gaat het tot het einide

Mijn_list = [1,2,3,4,5,6,7,8]
#optionele step index
b = Mijn_list[::1] #neemt elk item
print(b)
c = Mijn_list[::2] #neemt elk 2e item
print(c)
#ook een negatieve step, is een leuke manier om de list te reversen
d = Mijn_list[::-1]
print(d)
