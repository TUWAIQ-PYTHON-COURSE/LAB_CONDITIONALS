#1-Create a variable for the movie (choose any movie you like)
movie_name: str ="Red Notice"
#2-Create a variable of type int to hold the rating of the movie out of 5 . Give this movie 3
movie_rate : int=3
#3-Create a popularity score of type float , let it be 72.65
popularity_score : float=72.65


if movie_rate>=4 and popularity_score >80 :
   print("Highly recommended")



elif movie_rate >=3 or popularity_score >70 :
   print("I recommended it . It is good")



elif movie_rate <=2 and popularity_score >60 :
   print("You should check it out!")

else:  
   print("Don't watch it. It is a waste of time")
