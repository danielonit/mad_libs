def star_wars():
	adjective_one = (input("Enter an adjective: ")).replace(" ", "")
	noun_one = input("Enter a noun: ").replace(" ", "")
	adjective_two = input("Enter another adjective: ").replace(" ", "")
	place = input("Enter a place: ").replace(" ", "")
	adjective_three = input("Enter another adjective: ").replace(" ", "")
	adjective_four = input("Enter another adjective: ").replace(" ", "")
	vehicle = input("Enter a plural noun which is a vehicle: ").replace(" ", "")
	adjective_five = input("Enter another adjective: ").replace(" ", "")
	adjective_six = input("Enter another adjective: ").replace(" ", "")
	plural_noun_one = input("Enter a plural noun: ").replace(" ", "")
	adjective_seven = input("Enter another adjective: ").replace(" ", "")
	plural_noun_two = input("Enter another plural noun: ").replace(" ", "")
	plural_noun_three = input("Enter another plural noun: ").replace(" ", "")
	adjective_eight = input("Enter another adjective: ").replace(" ", "")
	noun_two = input("Enter another noun: ").replace(" ", "")
	verb_one = input("Enter a verb: ").replace(" ", "")
	adjective_nine = input("Enter another adjective: ").replace(" ", "")
	verb_two = input("Enter another verb: ").replace(" ", "")
	plural_noun_four = input("Enter another plural noun: ").replace(" ", "")
	job = input("Enter a plural noun which is a type of job: ").replace(" ", "")
	adjective_ten = input("Enter another adjective: ").replace(" ", "")
	verb_three = input("Enter another verb: ").replace(" ", "")
	adjective_eleven = input("Enter another adjective: ").replace(" ", "")

	print(f"\nStar wars is a {adjective_one} {noun_one} of {adjective_two} versus evil in a {place} far far away. There are {adjective_three} battles between {adjective_four} {vehicle} in {adjective_five} space and {adjective_six} duels with {plural_noun_one} called {adjective_seven}sabers. {plural_noun_two} called 'droids' are helpers and {plural_noun_three} to the heroes. A {adjective_eight} power called the {noun_two} {verb_one}s people to do {adjective_nine} things, like {verb_two} {plural_noun_four}. The jedi {job} use the force for the {adjective_ten} side and the Sith {verb_three} it for the {adjective_eleven} side.")
	
def the_space_shuttle():
	noun_one = input("Enter a noun: ").replace(" ", "")
	plural_noun_one = input("Enter a plural noun: ").replace(" ", "")
	verb_ing_one = input("Enter a verb ending in -ing: ").replace(" ", "")
	plural_noun_two = input("Enter another plural noun: ").replace(" ", "")
	city = input("Enter a city: ").replace(" ", "")
	plural_noun_three = input("Enter another plural noun: ").replace(" ", "")
	adjective_one = input("Enter an adjective: ").replace(" ", "")
	noun_two = input("Enter another noun: ").replace(" ", "")
	number_one = input("Enter a number: ").replace(" ", "")
	noun_three = input("Enter another noun: ").replace(" ", "")
	adjective_two = input("Enter another adjective: ").replace(" ", "")
	verb_one = input("Enter a verb: ").replace(" ", "")
	verb_two = input("Enter another verb: ").replace(" ", "")
	plural_noun_four = input("Enter another plural noun: ").replace(" ", "")
	verb_ing_two = input("Enter another verb ending in -ing: ").replace(" ", "")
	number_two = input("Enter another number: ").replace(" ", "")
	adverb = input("Enter an adverb: ").replace(" ", "")
	noun_four = input("Enter another noun: ").replace(" ", "")
	adjective_three = input("Enter another adjective: ").replace(" ", "")

	print(f"\nIn 1981, the U.S. launched the first real Space {noun_one}. It was named Columbia and was piloted by two brave {plural_noun_one}. They had practiced {verb_ing_one} for two years and were expert {plural_noun_two}. Columbia took off from {city.title()} using its powerful first-stage {plural_noun_three} and soared off into the {adjective_one} blue {noun_two}. At an altitude of {number_one} feet, it went into orbit around the {noun_three}. For people watching from Earth, it was a/an {adjective_two} sight to {verb_one}! Who could really {verb_two} that there were two {plural_noun_four} in space? It was mind {verb_ing_two}. After {number_two} orbits, the shuttle landed {adverb} at an air force {noun_four}. It was a/an {adjective_three} day for the U.S. space program.")

def school_is_almost_out():
	number = input("Enter a number: ").replace(" ", "")
	plural_body_parts = input("Enter a plural body part: ").replace(" ", "")
	plural_noun_one = input("Enter a plural noun: ").replace(" ", "")
	noun_one = input("Enter a noun: ").replace(" ", "")
	noun_two = input("Enter another noun: ").replace(" ", "")
	adjective_one = input("Enter an adjective: ").replace(" ", "")
	place = input("Enter a place: ").replace(" ", "")
	noun_three = input("Enter another noun: ").replace(" ", "")
	building_type = input("Enter a type of building: ").replace(" ", "")
	plural_noun_two = input("Enter another plural noun: ").replace(" ", "")
	verb_one = input("Enter a verb: ").replace(" ", "")
	adjective_two = input("Enter another adjective: ").replace(" ", "")
	plural_noun_three = input("Enter another plural noun: ").replace(" ", "")
	noun_three = input("Enter another noun: ").replace(" ", "")
	verb_two = input("Enter another verb: ").replace(" ", "")
	noun_four = input("Enter another noun: ").replace(" ", "")
	exclamation = input("Enter an exclamation: ").replace(" ", "")
	verb_three = input("Enter another verb: ").replace(" ", "")

	print(f"\nCan this day get any longer? We've been at school for {number} hours, and we're all struggling to keep our {plural_body_parts} open. We've sat through a lecture about {plural_noun_one}, taken a/an {noun_one} quiz in English class, and watched a movie about {noun_two} rights. And don't even mention the {adjective_one} food we had for lunch in (the) {place}. But thankfully it's almost time for the final {noun_three} to ring. And once it does, we can grab our backpacks, walk out of the {building_type}'s front doors, and head off to the {plural_noun_two} that we all love. It's not that we don't {verb_one} school and our {adjective_two} teachers-we do! But there's nothing better than leaving our {plural_noun_three} behind to go practice with the {noun_three}, {verb_two} a picture, or bake a/an {noun_four}, {exclamation}-that's the bell! We {verb_three} for after school!")

print("Hello and welcome to my Mad Libs game.")

while True:
	while True:
		rules = input("\nWould you like to know the rules: ")

		if rules.title() == "Yes" or rules.title() == "Y":
			print("\nOk! Here are the rules:")
			print("The computer acts as the “reader” and asks you,  the user, to fill in the blanks with adjectives, nouns, exclamations, colors, adjectives, and more. These words are inserted into the blanks and then the story is read aloud to hilarious results.")
			break

		elif rules.title() == "No" or rules.title() == "N":
			print("Ok! I won't show you the rules.")
			break
		
		else:
			print("I don't understand this input! Please try again.")

	while True:

		print("\nThere are three different game options.")
		game_options = input("Would you like to see the three options: ")

		if game_options.title() == "Yes" or game_options.title() == "Y":
			print("\nOk! Here are the three game options:")
			print("1) Star Wars")
			print("2) The Space Shuttle")
			print("3) School's Almost Out")
			break
		
		elif game_options.title() == "No" or game_options.title() == "N":
			print("\nOk! I won't show you the game options.")
			break

		else:
			print("\nI don't understand this input! Please try again.")

	while True:
		game_number = input("\nWould you like to play game one, two, or three: ")

		if game_number.title() == "One" or game_number == "1":
			print("\nYou chose game number one!")
			star_wars()
			break
		
		elif game_number.title() == "Two" or game_number == "2":
			print("\nYou chose game number two!")
			the_space_shuttle()
			break
		
		elif game_number.title() == "Three" or game_number == "3":
			print("\nYou chose game number three!")
			school_is_almost_out()
			break
	

	play_again = input("\nWould you like to play again: ")

	if play_again.title() == "Yes" or play_again.title() == "Y":
		continue

	elif play_again.title() == "No" or play_again.title() == "N":
		print("\nOk! Thank you for playing!")
		print("Shutting down now.")
		break
		
	else:
		print("I don't understand this input! Please try again.")
