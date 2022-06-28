import sys

Usage = f'''
        
        [*] Incorrect usage. Please try again.

        [*] Movie recommendation script
        [*] Usage: python {sys.argv[0]} "movie_name" movie_rating movie_popularity
        
        '''
# Check for correct usage
if len(sys.argv) < 2:
    print(Usage)
else:
    # define variables
    movie_name = str(sys.argv[1])
    movie_rating = int(sys.argv[2])
    movie_popularity = float(sys.argv[3])

    if (movie_rating >= 4) and (movie_popularity >= 80):
        print(f"{movie_name} is highly recommended.")
    elif (movie_rating >= 3) and (movie_popularity >= 70):
        print(f"I recommend {movie_name}. It is good.")
    elif (movie_rating <= 2) and (movie_popularity >= 60):
        print(f"You should check {movie_name} out!")
    else:
        print(f"Don't watch {movie_name}. It is a waste of time.")

