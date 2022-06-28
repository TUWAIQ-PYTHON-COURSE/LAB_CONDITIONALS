movie : str = "top gun"
rating : int = 3
pop : float = 72.65

if rating >= 4 and pop > 80.00 :
    print("Highly recommended")
elif rating >= 3 and pop > 70.00 :
    print ("I recommended it . It is good")
elif rating <= 2 and pop > 60.00 :
    print ("You should check it out!")
elif rating <= 2 and pop > 50.00 :
    print ("Don't watch it. It is a waste of time")