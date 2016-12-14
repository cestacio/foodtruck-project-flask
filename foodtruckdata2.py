# -*- encoding: utf-8 -*-

"""
this is a food truck project that will let the user know where a food truck 
is in san francisco on a specific day. 

we need to filter food truck by day, cuisine, and truck name. 
"""

from urllib2 import urlopen
from json import load

from foodtruckuser import * 
from testtruck import kettlecorn

FOODTRUCK_ENDPOINT = "https://data.sfgov.org/resource/6a9r-agq8.json"

def call_sfdataapi(endpoint):
	"""import data from sf open data"""

	response = urlopen(endpoint)
	return response

def load_sfdata(response):
	""" load data """

	json_obj = load(response)
	return json_obj

def clean_data(json_obj):
	""" parsing data in json_obj and returns a dictionary of cleaned up data """

	clean_data = {}

	for truck in json_obj:
		truck_name = truck['applicant'].lower()
		if 'fooditems' in truck:
			truck_cuisine = truck['fooditems'].lower()
		else:
			truck_cuisine = None
		if 'dayshours' in truck:
			truck_days = truck['dayshours'].lower()
		else:
			truck_days = None
		if 'locationdescription' in truck:
			truck_location = truck['locationdescription'].lower()
		else: 
			truck_location = None

		clean_data[truck_name] = truck_cuisine, truck_days, truck_location
	return clean_data 

def search_by_day(cleaned_data, username, user_day_pref):
	""" loop through data and searches by day """
	truck_days = None
	
	while truck_days == None: 
		if user_day_pref == 1:
			truck_days = ['mo-su', 'mo-fri', 'm', 'mo-sat']
		elif user_day_pref == 2:
			truck_days = ['mo-su', 'mo-fri', 'tu', 'mo-sat']
		elif user_day_pref == 3:
			truck_days = ['mo-su', 'mo-fri', 'w', 'mo-sat']
		elif user_day_pref == 4:
			truck_days = ['mo-su', 'mo-fri', 'th', 'mo-sat']
		elif user_day_pref == 5:
			truck_days = ['mo-su', 'mo-fri', 'f', 'mo-sat']
		elif user_day_pref == 6:
			truck_days = ['mo-su', 'sat', 'mo-sat']
		elif user_day_pref == 7:
			truck_days = ['mo-su','sun']
		else:
			print "That's not a valid choice. Try again."
			user_day_pref = int(raw_input("Select your choice between 1-7. "))


	display_recommendations(username)
	# this iterates over every single truck in cleaned data 
	for truck, info in cleaned_data.items():
		# this iterates over every day in truck days 
		for day in truck_days:
			if info[1] and day in info[1]:
				print truck, "is at ", info[2], "\n"

		
def search_by_cuisine(cleaned_data, user_food_pref, username):
	""" loop through data and searches by cuisine """

	display_recommendations(username)

	for truck,info in cleaned_data.items():
		if info[0] and user_food_pref in info[0]:			
			print truck, "is at ", info[2], "\n"

def search_by_truck(cleaned_data, username, user_truck_pref):

	display_recommendations(username)
	
	for truck,info in cleaned_data.items():
		if info[2] and user_truck_pref in truck: 	
			print truck, "is at", info[2], "\n"

# def add_new_profile(cleaned_data, username):

# 	display_recommendations(username)

# 	cleaned_data[username] = []
# 	return cleaned_data

# def add_user_pref(cleaned_data, username, user_truck_pref, user_food_pref, user_day_pref):

# 	display_recommendations(username)

# 	cleaned_data[username] = []

# 	cleaned_data[username].append(user_truck_pref, user_food_pref, user_day_pref)
# 	return cleaned_data

	
def main():
	# this is loading data
	response = call_sfdataapi(FOODTRUCK_ENDPOINT)
	foodtruck_list = load_sfdata(response)
	cleaned_data = clean_data(foodtruck_list)
	
	# this is where we prompt user for preferences
	
	username = prompt_user_for_username()

	while(True):

		display_menu()
		user_menu_choice = prompt_user_menu_choice()

		if user_menu_choice == "A":
			user_food_pref = prompt_user_for_cuisine()
			search_by_cuisine(cleaned_data, user_food_pref, username)

		if user_menu_choice == "B":
			print day_choices
			user_day_pref = int(raw_input("Select your choice between 1-7. "))
			search_by_day(cleaned_data, username, user_day_pref)

		if user_menu_choice == "C":
			user_truck_pref = str(raw_input("Where do you want to eat?"))
			search_by_truck(cleaned_data, username, user_truck_pref)

		# if user_menu_choice == "D":
		# 	pass
		# 	# save_user_truck_pref = str(raw_input("Please enter your favorite food truck."))
		# 	# add_user_pref(cleaned_data, username, save_user_truck_pref).append()

		elif user_menu_choice == "X":
			break


if __name__ == '__main__':
	main()