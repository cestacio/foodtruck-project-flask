# -*- encoding: utf-8 -*-

"""
this is a food truck project that will recommend a food truck to a user 
based on their preferences. 

we need to filter food truck by day, cuisine, and truck name. 
"""

from urllib2 import urlopen
from json import load

from foodtruckuser import * 

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
		truck_name = truck['applicant'].lower() # figure out why it thinks truck is a string 
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
	# print clean_data
	return clean_data 


response = call_sfdataapi(FOODTRUCK_ENDPOINT)
foodtruck_list = load_sfdata(response)
cleaned_data = clean_data(foodtruck_list)


def search_by_day(cleaned_data, username, user_day_pref):
	""" loop through data and searches by day """
	day_list = []
	cleaned_data = clean_data(foodtruck_list)
	truck_days = None
	
	while truck_days == None: 
		if user_day_pref == 1:
			truck_days = ['monday', 'mo-su', 'mo-fri', 'm', 'm/', 'mo-sat']
		elif user_day_pref == 2:
			truck_days = ['tuesday', 'mo-su', 'mo-fri', 'tu', 'mo-sat']
		elif user_day_pref == 3:
			truck_days = ['wednesday', 'mo-su', 'mo-fri', 'w', 'mo-sat']
		elif user_day_pref == 4:
			truck_days = ['thursday', 'mo-su', 'mo-fri', 'th', 'mo-sat']
		elif user_day_pref == 5:
			truck_days = ['friday', 'mo-su', 'mo-fri', 'f', 'mo-sat']
		elif user_day_pref == 6:
			truck_days = ['saturday', 'mo-su', 'sat', 'mo-sat']
		elif user_day_pref == 7:
			truck_days = ['sunday', 'mo-su','sun']
		else:
			print "That's not a valid choice. Try again."
			user_day_pref = int(raw_input("Select your choice between 1-7. "))

	# this iterates over every single truck in cleaned data 
	for truck, info in cleaned_data.items():
		# this iterates over every day in truck days 
		for day in truck_days:
			if info[1] and day in info[1]:
				# print truck, "is at ", info[2], "\n"

				day_list.append((truck, info[2]))
	print day_list
	return day_list


response = call_sfdataapi(FOODTRUCK_ENDPOINT)
foodtruck_list = load_sfdata(response)
cleaned_data = clean_data(foodtruck_list)
		

def search_by_cuisine(cleaned_data, user_food_pref, username):
	""" loop through data and searches by cuisine """

	cuisine_list = []
	cleaned_data = clean_data(foodtruck_list)

	for truck,info in cleaned_data.items():
		if info[0] and user_food_pref in info[0]:			
			# print truck, "is at ", info[2], "\n"

			cuisine_list.append((truck, info[2]))
	print cuisine_list
	return cuisine_list


response = call_sfdataapi(FOODTRUCK_ENDPOINT)
foodtruck_list = load_sfdata(response)
cleaned_data = clean_data(foodtruck_list)


def search_by_truck(cleaned_data, username, user_truck_pref):

	truck_list = []
	cleaned_data = clean_data(foodtruck_list)
	
	for truck,info in cleaned_data.items():
		if info and user_truck_pref in info: 	
		# print truck, "is at", info[2], "\n"
		
			truck_list.append((truck, info[2]))
	print truck_list
	return truck_list


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
			user_truck_pref = raw_input("Where do you want to eat?")
			search_by_truck(cleaned_data, username, user_truck_pref)

		elif user_menu_choice == "X":
			break


if __name__ == '__main__':
	main()
