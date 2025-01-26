print("WELCOME TO HOGWARTS SCHOOL OF WITCHCRAFT AND WIZARDRY")

gryffindor = []
ravenclaw = []
slytherin = []
hufflepuff = []

while True:

    input_name = input("What is your name?: ")
    if input_name.endswith("a") or input_name.endswith("A"):
        print(" MUGGLE! You are not on the masterlist")
        break
    else:
        movie_genre = input("What movie genre you like?: ")    