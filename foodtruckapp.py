from flask import Flask, request, render_template
from foodtruckdata import *


app = Flask(__name__)
# the app is an instance of Flask


response = call_sfdataapi(FOODTRUCK_ENDPOINT)
foodtruck_list = load_sfdata(response)
cleaned_data = clean_data(foodtruck_list)
# print type(cleaned_data)


@app.route('/form')
def say_hello():
    """Show hello.html template. This is the welcome page. """
    return render_template('hello.html')


@app.route('/truckname')
def foodname():
	"""Show truckname.html template."""
	return render_template('truckname.html')


@app.route('/foodtype')
def foodtype():
    """Show foodtype.html template."""
    return render_template('foodtype.html')


@app.route('/days')
def days():
    """Show hello.html template."""
    return render_template('days.html')


@app.route('/foodrecs')
def foodrecs_foodtype():
	"""Show food truck recommendations based on food type."""
	player = request.args.get("person")
	user_food_pref = request.args.get("food")
	cleaned_data = clean_data(foodtruck_list)
	cuisine_list = search_by_cuisine(cleaned_data, user_food_pref, player)

	# print cuisine_list
	return render_template('foodrecs.html', 
							search_by_cuisine=cuisine_list, 
							name=player)


@app.route('/foodrecsday')
def foodrecs_days():
	"""Show food truck recommendations based on day"""
	player = request.args.get("person")
	user_day_pref = int(request.args.get("day"))
	cleaned_data = clean_data(foodtruck_list)
	day_list = search_by_day(cleaned_data, player, user_day_pref)

	return render_template('foodrecsday.html', 
							search_by_day=day_list, 
							name=player)


@app.route('/foodrecsname')
def foodrecs_name():
	"""Show food truck recommendations based on truck name"""
	player = request.args.get("person")
	user_truck_pref = request.args.get("truck")
	cleaned_data = clean_data(foodtruck_list)
	truck_list = search_by_truck(cleaned_data, player, user_truck_pref)

	# print truck_list
	return render_template('foodrecsname.html', 
							search_by_truck=truck_list, 
							name=player)


if __name__ == "__main__":
    app.run(debug=True)
