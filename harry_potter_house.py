print("WELCOME TO HOGWARTS SCHOOL OF WITCHCRAFT AND WIZARDRY")
gryffindor = 0
ravenclaw = 0
slytherin = 0
hufflepuff = 0
while True:

    input_name = input("What is your name?: ")
    if input_name.endswith("a") or input_name.endswith("A"):
        print("MUGGLE! YOU ARE NOT WELCOME!!!")
        break

    print("WELCOME! YOU MAY START YOUR SORTING JOURNEY")

    while True:

        movie_genre = input("What is your favorite movie genre?: ")

        if movie_genre == "action":
            gryffindor += 1
        elif movie_genre == "science fiction":
            ravenclaw += 1
        elif movie_genre == "horror":
            slytherin += 1
        elif movie_genre == "drama":
            hufflepuff += 1  
            break 
        else:
            print("Choose among horror, action, science fiction, and drama only!")  

    while True:

        animal = input("Which animal would you like to be a pet?: ")

        if animal == "cat":
            gryffindor += 1
        elif animal == "owl":
            ravenclaw += 1
        elif animal == "toad":
            slytherin += 1
        elif animal == "rat":
            hufflepuff += 1
            break
        else:
            print("Choose among cat, owl, toad, or cat!")

    while True:
          
        personality = input("Are you shy, confident, friendly, or arrogant?: ")

        if personality == "confident":
            gryffindor += 1
        elif personality == "shy":
            ravenclaw += 1
        elif personality == "arrogant":
            slytherin += 1
        elif personality == "friendly":
            hufflepuff += 1
            break
        else:
            print("Choose among the given choices!")   
    
  
