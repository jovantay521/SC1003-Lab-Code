# Coding Exercise 5a

def get_colour(colour):
    """takes string colour as input and returns integer value of colour"""
    keep_loop = True
    no_of_tries = 0
    
    while keep_loop:
        try:
            colour_input = int(input("Enter the " + colour + " value (0-255): "))
            if 0 <= colour_input <= 255:
                return colour_input
            
        except ValueError:
            print("Invalid colour value")
        
        no_of_tries += 1
        
        if no_of_tries >= 3:
            keep_loop = False
    
    print("Exceeded 3 tries. Setting " + colour + " value to 0")
    return 0
