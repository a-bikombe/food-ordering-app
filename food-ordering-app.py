def food_ordering_app():
	choice = input("Enter the food that you want: ");
	quantity = input("Enter the quantity: ");

	food_database = {
		"burger" : 5.99,

	}

	total = food_database[choice] * float(quantity);

	return total;

print("Your total is $", food_ordering_app());