#functions in lists

lucky_numbers = [4,8,12,13,23,53]
friends = ["Henk", "Lisa", "Dave", "Jane", "Oscar"]

# wekunnee ook individuele elemeenten bij lists toevoegen
friends.append("Dragnball")

#insert neem 2 paramaetes
friends.insert(1, "Bello") #dit gaat de overige elementen van de list naar rechts duwne
#we kunnenn zaken wegehalen uit lists
friends.remove("Henk")
#we kunnen de hele list leeggooien
#friends.clear()
#we kunnen het laatste element van een list eriut poppen met pop
friends.pop()
print("item pop");item_pop = friends.pop()
print(item_pop)
print(friends)

#We kunnen ook zoeken naar elementen in de lists bv zoeken naar Henk
print(friends.index("Bello")) # dit gaat me de index vertellen, als dit niet voorkomt kkrijgen we een error

#we kunnen kijkenn hoe vaak een elemetn voorkomt in een lists
friends2 = ["Henk", "Lisa", "Dave", "Jane", "Oscar", "Oscar", "Oscar"]
print("Oscar??")
#print("In friends 2 komt Oscar " + str(print(friends2.count("Oscar"))) +" keer voor")
print(friends2.count("Oscar"))
