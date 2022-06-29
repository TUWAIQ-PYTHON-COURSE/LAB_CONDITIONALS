
#- Create a variable for the movie (choose any movie you like)

movie = "zero"

#- Create a variable of type int to hold the rating of the movie out of 5 . Give this movie 3

rating : int = 5
movie_rating : int = 3
# - Create a popularity score of type float , let it be 72.65
popularity_score : float = 72.65

# if statement function 

if movie_rating  >= 4 or popularity_score > 80:
    print("Highly recommended")
elif movie_rating >= 3 and popularity_score > 70:
    print("I recommended it . It is good")
elif movie_rating <= 2 or popularity_score < 60:
    print("You should check it out!")
else:
     
     print("Don't watch it. It is a waste of time")











