print("WELCOME TO HOGWARTS SCHOOL OF WITCHCRAFT AND WIZARDRY")
gryffindor = 0
ravenclaw = 0
slytherin = 0
hufflepuff = 0

with open("hogwarts_house_result.txt", "a") as file:
  while True:
    input_name = input("What is your name?: ")

    if input_name.endswith("a") or input_name.endswith("A"):
      print("MUGGLE! YOU ARE NOT WELCOME!!!")
      file.write(f"Muggle detected: {input_name}\n")
      break

    print("WELCOME! YOU MAY START YOUR SORTING JOURNEY")
    file.write(f"Student name: {input_name}\n")

    while True:
      movie_genre = input("What is your favorite movie genre?: ")

      if movie_genre in ["action", "science fiction", "horror", "drama"]:
        if movie_genre == "action":
          gryffindor += 1
        elif movie_genre == "science fiction":
          ravenclaw += 1
        elif movie_genre == "horror":
          slytherin += 1
        elif movie_genre == "drama":
          hufflepuff += 1
        file.write(f"Movie Genre: {movie_genre}\n")  
        break 
      else:
        print("Choose among horror, action, science fiction, and drama only!")  

    while True:
      animal = input("Which animal would you like to be a pet?: ")

      if animal in ["cat", "owl", "toad", "rat"]:
        if animal == "cat":
          gryffindor += 1
        elif animal == "owl":
          ravenclaw += 1
        elif animal == "toad":
          slytherin += 1
        elif animal == "rat":
          hufflepuff += 1
        file.write(f"Preferred pet: {animal}\n")
        break
      else:
        print("Choose among cat, owl, toad, or cat!")

    while True:
      personality = input("Are you shy, confident, friendly, or arrogant?: ")

      if personality in ["confident", "shy", "arrogant", "friendly"]:
        if personality == "confident":
          gryffindor += 1
        elif personality == "shy":
          ravenclaw += 1
        elif personality == "arrogant":
          slytherin += 1
        elif personality == "friendly":
          hufflepuff += 1
        file.write(f"Personality:{personality}\n")
        break
      else:
        print("Choose among the given choices!")

    while True:
      attribute = input("Do you rather be brave, smart, patient, or ambitious?: ")

      if attribute in ["brave", "smart", "patient", "ambitious"]:
        if attribute == "brave":
          gryffindor += 1
        elif attribute == "smart":
          ravenclaw += 1
        elif attribute == "ambitious":
          slytherin += 1
        elif attribute == "patient":
          hufflepuff += 1
        file.write(f"Attribute: {attribute}\n")
        break  
      else:
        print("Choose among the choices!") 

    while True:
      quidditch = input("Which position would you most likely to play? bludger, keeper, seeker, or chaser: ")

      if quidditch in ["bludger", "keeper", "seeker", "chaser"]:
        if quidditch == "bludger":
          gryffindor += 1
        if quidditch == "keeper":
          ravenclaw += 1
        if quidditch == "seeker":
          slytherin += 1
        if quidditch == "chaser":
          hufflepuff += 1
        file.write(f"Qudditch position: {quidditch}\n")
        break  
      else:
        print("Choose among the choices!")

    while True:
      character = input("Who would you rather be? Snape, Cedric, Hagrid, or Luna?: ")

      if character in ["hagrid", "Luna", "Snape", "Cedric"]:
        if character == "hagrid":
          gryffindor += 1
        if character == "Luna":
          ravenclaw += 1
        if character == "Snape":
          slytherin += 1
        if character == "cedric":
          hufflepuff += 1
        file.write(f"Fave character: {character}\n")
        break  
      else:
        print("Choose among the choices!")                                              

    house_points = {
        "Gryffindor": gryffindor,
        "Ravenclaw": ravenclaw,
        "Slytherin": slytherin,
        "Hufflepuff": hufflepuff
    }

    sorted_house = max(house_points, key=house_points.get)
    print("CONGRATULATIONS!! YOU ARE.....")
    print(sorted_house)
    file.write(f"Sorted House: {sorted_house}\n")

    while True:
        another_try = input("Do you wwant to sort another one?: ").lower()
        if another_try in ["yes", "no"]:
            break
        else:
            print("Invalid Choice")
    if another_try != "yes":
        print("COLLOPORTUS")
        break
      
        