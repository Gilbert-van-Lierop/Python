friends = ["Henk", "Lisa", "Dave", "Jane", "Oscar"]
lucky_numbers = [4,8,12,13,23,53]

#We kunnen 2 lists bij elkaar toeveogen
friends.extend(lucky_numbers)
print(friends)


#maak een list met meerdere elementen
new_list = [0]  * 5
print("new list is :"); print(new_list)

#copy
print("100 friends")
friends100 = friends.copy()
print(friends100)

friends2 = ["Henk", "Lisa", "Dave", "Jane", "Oscar", "Oscar", "Oscar"]
#remove items form list
my_list = ["banana","cherry", "apple"]
item = my_list.remove("banana")
print(my_list)

friends_copy = friends2

print(friends_copy)
friends_copy.append("lemon")
print(friends_copy)
print(friends2)
#omdat beide lists met deze methode naar hetzelfde verwijzen in geheugen

#list comprehension, kunnne we een njieuw list maken uit een bestaande lists
last_list =[1,2,3,4,5]
b = [i for i in last_list]

print(last_list)
print(b)
