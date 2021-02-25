cars=100
space_in_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_car
average_passenger_per_car=passengers/cars_not_driven

print("there are",cars,"cars available")
print("There are ",drivers,"drivers Available")
print("There will be",cars_not_driven,"Empty card today")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passenger_per_car,"in each car.")
