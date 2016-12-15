
day_choices = """
		When do you want to eat? 
		Press:
		1 for Monday
		2 for Tuesday
		3 for Wednesday 
		4 for Thursday
		5 for Friday
		6 for Saturday
		7 for Sunday
		"""	


def prompt_user_for_username():
	username = raw_input("Welcome to SF Food Truck Finder! What is your name? ")
	return username


def prompt_user_for_cuisine():
	user_food_pref = str(raw_input("What do you want to eat? "))
	return user_food_pref	


def prompt_user_for_truckname():
	user_truck_pref = str(raw_input("Where do you want to eat?"))
	return user_truck_pref


def display_menu():
	print """
		Hungry? Please select from the options below:

		A = Search By Food Type
		B = Search By Day
		C = Search By Truck Name
		X = exit SF Food Truck Finder
	"""


def prompt_user_menu_choice():
	user_menu_choice = raw_input("Please select from above: ").upper()
	return user_menu_choice


def display_recommendations(username):
	print "Hey, " + username + "! " + "Here are my recommendations: "


def main():
	# this is just for testing
	username = prompt_user_for_username()
	user_food_pref = prompt_user_for_cuisine()
	display_user_recs = clean_data()

	print "Hey, " + username + "! " + user_food_pref + " sounds great! " + "Here are my recommendations: "
	print display_user_recs


if __name__ == '__main__':
	main()
