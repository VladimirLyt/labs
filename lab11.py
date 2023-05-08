def prog1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Restaurant name: {self.restaurant_name}")
            print(f"Cuisine type: {self.cuisine_type}")

        def open_restaurant(self):
            print("The restaurant is open")

    newRestaurant = Restaurant("Pizza Hut", "Italian")
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()
def prog2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print("Restaurant name:", self.restaurant_name)
            print("Cuisine type:", self.cuisine_type)

        def open_restaurant(self):
            print("The restaurant", self.restaurant_name, "is now open.")

    italian_restaurant = Restaurant("Mamma Mia", "Italian")
    chinese_restaurant = Restaurant("China Wok", "Chinese")
    mexican_restaurant = Restaurant("El Sombrero", "Mexican")

    italian_restaurant.describe_restaurant()
    chinese_restaurant.describe_restaurant()
    mexican_restaurant.describe_restaurant()
def prog3():
    class Restaurant:
        def __init__(self, name, cuisine_type, rating):
            self.name = name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"{self.name} is a {self.cuisine_type} restaurant with a rating of {self.rating}.")

        def update_rating(self, new_rating):
            self.rating = new_rating
    # Создаем объект класса Restaurant с начальным рейтингом 4.3
    restaurant = Restaurant("The Green Garden", "vegetarian", 4.3)

    # Выводим описание ресторана
    restaurant.describe_restaurant()

    # Обновляем рейтинг ресторана
    restaurant.update_rating(4.8)

    # Выводим описание ресторана с обновленным рейтингом
    restaurant.describe_restaurant()
