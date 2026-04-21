# You have 4 films in the dictionary with the age and number of seats available as indicated below. Write a programme to ask for a film and check for the person that he is eligible to watch movie, also check ticket availability and movie availability in the cinema.
#        "War": [3,5],
#         "Bourne": [18,5],
#         "Gully boy": [15,5],
#         "Uri":[12, 5]


movies = {
    "War": [3,5],
    "Bourne": [18, 5],
    "Gully boy": [15, 5],
    "Uri": [12, 5]
}

movie = input("Enter movie name: ")
age = int(input("Enter your age: "))

if movie in movies:
    required_age, seats = movies[movie]

    if age >= required_age:
        if seats > 0:
            print("You can watch the movie !")
            print("Seats available: ", seats)
        else:
            print("Sorry, no seats available.")
    else:
        print("You are not eligible for this movie.")
else:
    print("Movie not available in cinema.")
    
