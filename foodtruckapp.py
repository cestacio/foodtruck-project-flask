from flask import Flask, request, render_template
from foodtruckdata import *



app = Flask(__name__)
# the app is an instance of Flask

response = call_sfdataapi(FOODTRUCK_ENDPOINT)
foodtruck_list = load_sfdata(response)
cleaned_data = clean_data(foodtruck_list)
print type(cleaned_data)

@app.route('/form')
def say_hello():
    """Show hello.html template."""
    return render_template('hello.html')

# COMPLIMENTS = ["awesome", "clever", "wonderful", "fierce", "strong"]

# @app.route('/greet')
# def greet_person():
#     """Return customized compliment along with person name."""

#     player = request.args.get("person")
#     nice_thing = choice(COMPLIMENTS)
#     return render_template('compliments.html',
#                            name=player,
#                            compliment=nice_thing)


@app.route('/foodrecs')
def foodrecs():
	player = "charmaine" #request.args.get("person")
	user_food_pref = "tacos" #request.args.get("food")
	cleaned_data = clean_data(foodtruck_list)
	cuisine_list = search_by_cuisine(player, user_food_pref, cleaned_data)
	# print cuisine_list
	return render_template('foodrecs.html', 
							search_by_cuisine=str(cuisine_list), 
							name=player)


if __name__ == "__main__":
    app.run(debug=True)