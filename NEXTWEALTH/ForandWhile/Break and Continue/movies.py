############## Problem  1 #################### 
#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the color"
#Continue until they is atleast 3 movies they both like

#init variables
movies = input("What movies you like ? :")
#convert movies into a List
movies = movies.lower()
movieList = movies.split()

commonMovies = []
commonMovieCount = 0
while (True) :
    #ask the second friend for one movie at a time
    movie = input (" What movies you like ? : " ).lower()
    #Check if this movie is in the movie list
    #if present, 
    if movie in movieList:
        print(f"You both like {movie} movie")
        commonMovies.append(movie)
        commonMovieCount += 1
    else:
        print("Try again ! ")

    #check if we reached the max
    if(commonMovieCount >= 3):
        break;

print ("Common movies that you both like : ",commonMovies) #FillinMissingCode - list all the common movies