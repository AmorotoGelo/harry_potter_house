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

        if movie_genre == "action":
            gryffindor.append(input_name)
        elif movie_genre == "science fiction":
            ravenclaw.append(input_name)
        elif movie_genre == "horror":
            slytherin.append(input_name)
        elif movie_genre == "drama":
            hufflepuff.append(input_name)    
        else:
            print("Choose among horror, action, science fiction, and drama only")  

        
        animal = input("Which animal would you like to be a pet?: ")

        if animal == "cat":
            gryffindor.append(input_name)
        elif animal == "owl":
            ravenclaw.append(input_name)
        elif animal == "toad":
            slytherin.append(input_name)
        elif animal == "rat":
            hufflepuff.append(input_name)
        else:
            print("Choose among cat, owl, toad, or cat: ")                
        

