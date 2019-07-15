FILE_PATH = "scores.txt"


def print_ratings(filename):
    """Print restaurant ratings in alphabetical order.
    """

    file_data = open(filename)

    restaurant_ratings = {}

    for line in file_data:
        line = line.rstrip()

        restaurant_name, rating = line.split(":")
        restaurant_ratings[restaurant_name] = rating

    user_restaurant = input("Add a restaurant: ")

    restaurant_ratings[user_restaurant]= input("Give a score: ")

    for rest_name, rest_rating in sorted(restaurant_ratings.items()):
        print(f'{rest_name} is rated at {rest_rating}.')

print_ratings(FILE_PATH)