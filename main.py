
movie:str = "Forest Gump"
rating:int = 3

popularity:float = 72.65

if (rating > 4) or (popularity > 80):
    print("Highly recommended.")
elif (rating > 3) or (popularity > 70):
    print("I recommend it. It is good.")
elif (rating > 2) or (popularity > 60):
    print("You should check it out!")
else:
    print("Don't watch it. It is a waste of time.")


