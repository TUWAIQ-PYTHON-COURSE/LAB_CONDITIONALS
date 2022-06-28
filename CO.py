# Create a variable for the movie (choose any movie you like)
movie_name : int = "good will hunting"

# Create a variable of type int to hold the rating of the movie out of 5 . Give this movie 3
movie_rating : int = 3
# im not ok puting a 3 star rating, its a 5 for me!

# Create a popularity score of type float , let it be 72.65
popularity_score : float = 72.65

# Check if the movie rating is 4 or greater and the popularity is greater than 80 , print "Highly recommended"
# else if the movie rating is 3 or greater and the popularity is greater than 70 , print "I recommended it . It is good"
# else if the movie rating is 2 or less and the popularity is greater than 60 , print "You should check it out!"
# else  the movie rating is 2 or less and the popularity is less than 50 , print "Don't watch it. It is a waste of time"

if movie_rating >= 4 and popularity_score > 80 :
    print("highly recommended!")
elif movie_rating >= 3 and popularity_score > 70 :
    print("i recommended it . it is good!")
elif movie_rating <=2 and popularity_score > 60 :
    print("you should check it out!")
else:
    print("dont watch it. its a waste of time")