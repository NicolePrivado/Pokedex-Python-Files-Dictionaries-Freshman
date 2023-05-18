#Andrea Nicole G. Privado
#privado_07.py
#This program allows the user to add, view and delete pokemons in the pokedex. 
def choice():							#function that shows the menu and ask for the user choice
	print("*******POKEDEX*******")
	print("* 1.Add Pokemon     *")
	print("* 2.View Pokemon    *")
	print("* 3.Delete Pokemon  *")
	print("* 4.Save            *")
	print("* 5.Load            *")
	print("* 6.Exit            *")
	print("*********************")
	return int(input(" Choice: "))
def add():								#fuction that adds a pokemon to the pokedex, iff the entered pokemon does not exist in the pokedex
	name = input("Enter Pokemon name: ")
	name = name.capitalize()			#name capitalization
	if name not in pokedex: 			#checking if name is not in the pokedex
		temp = {}
		temp["name0"] = name
		temp["type0"] = input("Pokemon type: ")
		temp["species"] = input("Species: ")
		temp["height"] = float(input("Height (m): "))
		temp["bxp"] = int(input("Base experience: "))
		pokedex[name]= temp
		print(name, "successfully added!")
	else:						
		print("Pokemon already exists!")
def view(): 							#function for viewing the pokemons in the pokedex
	if pokedex =={}:   				 	#checking if the pokedex is an empty dictionary
		print("There are no Pokemons in the Pokedex!")
	else:												#if it is in the dictionary, it will print the all the pokemon's name, type, species, height in meters, and base experience in the pokedex.
		print("The Pokemons in your Pokedex are:")
		for p in pokedex:      				#loop for modifying each element in the pokedex
			#printing pokemon's description
			print(pokedex[p]["name0"]+":")
			print(" -Type:",pokedex[p]["type0"])
			print(" -Species:",pokedex[p]["species"])
			print(" -Height (m):",pokedex[p]["height"])
			print(" -Base XP:",pokedex[p]["bxp"])
			print()
def delete():								#function for deleting pokemon in the pokedex
	name1=input("Enter Pokemon name: ")
	name1 = name1.capitalize()
	if name1 in pokedex:					#checking if the entered pokemon is in the pokedex
		del pokedex[name1]					#deleting the pokemon from the pokedex
		print(name1, "successfully deleted!")
	else:
		print(name1,"does not exist in Pokedex!")
		
def save():									#function for saving
	if pokedex == {}:
		print("There are no Pokemons in the Pokedex to save!")
	else:
		fp = open("pokemon.txt", "w")
		for element in pokedex:
			temp = element+","
			temp = temp+pokedex[element]["type0"]+","
			temp = temp+pokedex[element]["species"]+","
			temp = temp+str(pokedex[element]["height"])+","
			temp = temp+str(pokedex[element]["bxp"])+"\n"
			fp.write(temp)		#writing on the docu
		
		fp.close()
		print("Pokedex successfully saved!")
def load():						#function for load
	pokedex.clear()		#overwriting		
		
	fp = open("pokemon.txt", "r")
	for line in fp:
		line=line[:-1]
		data = line.split(",")
		name = data[0]
		pokedex[name] ={"name0": data[0],"type0": data[1] , "species" : data[2], "height": data[3], "bxp": data[4]}   #returning to dictionary
	fp.close()

	print("Pokedex successfully loaded!")

pokedex={}    	#empty dictionary of the pokedex
x = 0				#variable for the choice
while x != 6:
	x = choice() 	#assigning the value of choice() to x
	if x == 1:		#choice for adding pokemon
		add()
	elif x == 2:	#choice for viewing pokedex
		view()
	elif x == 3:	#choice for deleting pokemon
		delete()
	elif x == 4:	#choice for saving
		save()
	elif x == 5:	#choice for loading
		load()
	elif x == 6:	#exit
		break
	else:			#when entered invalid choices
		print("Invalid Choice!")
print("Goodbye!")				#if the user entered 4, the program will exit
