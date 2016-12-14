# -*- encoding: utf-8 -*-

"""
this is a food truck project that will let the user know where a food truck 
is in san francisco on a specific day. 

we need to filter food truck by day.

add on's: filter by cuisine

"""

# import data from sf open data

# load data 

# loop through data and set parameters to search for 

from urllib2 import urlopen
from json import load

# from testtruck import kettlecorn

FOODTRUCK_ENDPOINT = "https://data.sfgov.org/resource/6a9r-agq8.json"

def call_sfdataapi(endpoint):
	response = urlopen(endpoint)
	return response

def load_sfdata(response):
	json_obj = load(response)
	return json_obj

def clean_data(json_obj):
	clean_data = {}
	# print clean_data

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
		# for key,value in truck.items():
		# 	key = key.lower()
		# 	value = value.lower()
		# 	# print key
		
		# 		# value_value = value_value.lower()
		# 	print value
	
# lots of conditionals and parsing!! parse days and hours, make sure it is searchable, normalize data

# screen for location, expired permits 
# another idea - creating an object based on user preferences, ask questions
# ahead of time. given user preferences, provide suggestions 

def search_by_day(clean_data):
	# return foodtruck_list[0]
	# for truck in clean_data:
	# # truck = kettlecorn
	# 	# truck_name = truck['applicant']
	# 	if 'dayshours' in truck:
	# 		truck_avail_list = truck['dayshours'].split(':')

	# 		# create clean dictionary	

	# 		# truck_days, truck_hours = truck['dayshours'].split(':')
	# 		print truck_name, truck_avail_list
	# 		# print truck_days, truck_hours
		if truck_days == 'Mo-Su':
			truck_days = {'Monday': truck_hours,'Tuesday': truck_hours, 
						'Wednesday': truck_hours, 'Thursday': truck_hours,
						'Friday': truck_hours, 'Saturday': truck_hours, 
						'Sunday': truck_hours}
		else:
			None
			# print truck_name, truck_avail_list
		return truck_name, truck_days
		# else:
		# return truck_name		

def search_by_cuisine(clean_data):
	# search_cuisine = "chicken"
	# for truck in foodtruck_list:
	# 	if 'fooditems' in truck:
	# 		truck_cuisine = truck['fooditems'].split(':')
	# 		if 'tacos'.title() in truck_cuisine:
	# 			print truck['applicant'], truck_cuisine
	response = call_sfdataapi(FOODTRUCK_ENDPOINT)
	foodtruck_list = load_sfdata(response)
	cleaned_data = clean_data(foodtruck_list)

	for place,info in cleaned_data.items():
		if info[0] and 'burrito' in info[0]:
			print place,info

# search off  clean data

def main():
	# response = call_sfdataapi(FOODTRUCK_ENDPOINT)
	# foodtruck_list = load_sfdata(response)
	# print search_by_day(foodtruck_list)
	# print search_by_cuisine(foodtruck_list)
	# cleaned_data = clean_data(foodtruck_list)
	# print cleaned_data
	print search_by_cuisine(clean_data)
	# print search_by_day(clean_data)


if __name__ == '__main__':
	main()