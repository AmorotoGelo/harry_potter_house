print("WELCOME TO HOGWARTS SCHOOL OF WITCHCRAFT AND WIZARDRY")
gryffindor = []
ravenclaw = []
slytherin = []
hufflepuff = []
while True:

    input_name = input("What is your name?: ")
    if not input_name.endswith("a") or input_name.endswith("A"):
        print("Welcome! You may proceed: ")
        
        movie_genre = input("What is your favorite movie genre?: ")

        if movie_genre == "action":
            gryffindor.append(input_name)
        elif movie_genre == "science fiction":
            ravenclaw.append(input_name)
        elif movie_genre == "horror":
            slytherin.append(input_name)
        elif movie_genre == "drama":
            hufflepuff.append(input_name)    
        else:
            print("Choose among horror, action, science fiction, and drama only!")  

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
            print("Choose among cat, owl, toad, or cat!")

               
        personality = input("Are you shy, confident, friendly, or arrogant?: ")

        if personality == "confident":
            gryffindor.append(input_name)
        elif personality == "shy":
            ravenclaw.append(input_name)
        elif personality == "arrogant":
            slytherin.append(input_name)
        elif personality == "friendly":
            hufflepuff.append(input_name)
        else:
            print("Choose among the given choices!")   

        if ravenclaw > gryffindor or ravenclaw > slytherin or ravenclaw > hufflepuff:
          print("CONGRAATULATIONS WIZARD: You are RAVENCLAW!")    
          break    
    
    else:
        print("MUGGLE! YOU ARE NOT WELCOME!!!")
        break


