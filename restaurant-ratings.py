from sys import argv
from random import randint

def get_restaurant_entry():
    """ Prompt the user for a restaurant name and rating. Store it in the dictionary as key and value."""    
    name = raw_input("What is your name?\n>> ")
    print "Hello, %s.\n" % (name)
    restaurant = raw_input("Give me a restaurant name:\n>> ")
    rating = int(raw_input("Give me a restaurant rating:\n>> "))
    return restaurant, rating



def update_random_rating():
    """Prompt user to update score of a random restaurant from the existing list. Continue prompting until user types q. Print all ratings in alpha order by name."""
 
    
    current_restaurant_dict = show_restaurant_ratings()
    current_restaurant_names = current_restaurant_dict.keys()

    name = raw_input("What is your name?\n>> ")
    
    while True:

        user_quit = raw_input("To quit, type 'q' now. To update our ratings, type anything else. \n>> ")
        if user_quit.lower() == 'q':
            # print new dictionary
            for rest, rating in sorted(current_restaurant_dict.iteritems()):
                print "{} is rated at {}.".format(rest,rating)
            break
        else:
            random_restaurant_index = randint(0,len(current_restaurant_names)-1)
            random_restaurant_name = current_restaurant_names[random_restaurant_index]
            random_restaurant_rating = current_restaurant_dict[random_restaurant_name]

            print "Hello, %s. %s is currently rated %r. What is your updated rating?" % (name, random_restaurant_name, random_restaurant_rating)

            new_rating = int(raw_input("\n>> ")) 

            # overwrite restaurant rating in dictionary
            current_restaurant_dict[random_restaurant_name] = new_rating

    






def show_restaurant_ratings():
    """Read the file, then print the ratings in alphabetical order by restaurant.

    Sample output:

    $ python restaurant-ratings.py
    Andalu is rated at 3.
    Arinell's is rated at 4.
    Bay Blend Coffee and Tea is rated at 3.
    Casa Thai is rated at 2.

    """

    script_name, file_name = argv
    rest_dict = {}
    
    #Open file and clean up data. Set dictionary key-value pairs according to index in line.        
    with open(file_name) as ratings_file:
        
        for line in ratings_file:
            restaurant, rating = line.rstrip().split(":") #unpack list and assign to restaurant and rating variables
            # restaurant:rating = restaurant_and_rating[0]
            # rating = restaurant_and_rating[1]
            
            #create key and value pair in dictionary
            rest_dict[restaurant] = rating
        
        # go through each key-value tuple in dictionary in alpha order by key
        # for rest, rating in sorted(rest_dict.iteritems()):
        #     print "{} is rated at {}.".format(rest,rating)

    # new_restaurant, new_rating = get_restaurant_entry()

    # rest_dict[new_restaurant] = new_rating

    #go through each key-value tuple in dictionary in alpha order by key
    for rest, rating in sorted(rest_dict.iteritems()):
        print "{} is rated at {}.".format(rest,rating)

    return rest_dict



update_random_rating()