## You want to recommend a movie to a friend based on the rating and popularity . To accomplish this do the following : 

#- Create a variable for the movie (choose any movie you like)
movie_name : str = "Top Gun"

#- Create a variable of type int to hold the rating of the movie out of 5 . Give this movie 3
movie_rate : int = 3 

#- Create a popularity score of type float , let it be 72.65
movie_score : float = 72.65 
#- Using an if statement 
if movie_name == "Top Gun":
    print("This is the movie a choose")

elif movie_name == "Fast & Furious":
    print("This is not the movie a choose")


#- - Check if the movie rating is 4 or greater and the popularity is greater than 80 , print "Highly recommended"

if movie_rate == 4 and movie_score < 80 :
    print("Highly recommended")
#- - else if the movie rating is 3 or greater and the popularity is greater than 70 , print "I recommended it . It is good"
elif movie_rate == 3 and movie_score < 70 :
    print("I recommended it . It is good")
#- - else if the movie rating is 2 or less and the popularity is greater than 60 , print "You should check it out!"
elif movie_rate == 2 and movie_score > 60 :
    print("You should check it out!")
#-  - else  the movie rating is 2 or less and the popularity is less than 50 , print "Don't watch it. It is a waste of time"
elif movie_rate == 2 and movie_score < 50 :
    print("Don't watch it. It is a waste of time")

else:
    print("End the page")