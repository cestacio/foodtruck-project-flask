class Userpref(object):
	def __init__(self, name_first, day, cuisine):
		self.name_first = name_first
		self.day = day
		self.cuisine = cuisine

def main():
	print "Hi, welcome to SF Food Truck Finder!"
	print "Let me collect your preferences."

	name = raw_input("What's your name?")

	user1 = userpref(name)

	food = raw_input("What do you want to eat?")
		user1.cuisine = food
		user1.day = day
