# Jack Berendt
# Thursday September 19 2024
# Purpose: To create a Flower class and multiple flower objects.


class Flower: # This line defines the class Flower. 
    def __init__(self, name): # This is the constructor of the Flower. When a flower object is instantiated, the arguments passed to this function will be assigned to attributes of the object.
        self.name = name # This line assigns the name passed to the constructor to the newly created flower object.

    def grow(self): # This is a method within the Flower class. The method can be called from any object instantiated from the Flower class.
        print("The " +self.name + " is growing.") # This prints a message that includes the flower object's name.

    def bloom(self): # This is another method within the Flower class.
        print("The " + self.name + " is blooming.") # This prints a message that includes the flower object's name.

def main(): # The main function of the python program. This runs when the program is executed.
    flower1 = Flower("Rose") # This defines a flower with the name Rose from the Flower class.
    flower1.grow() # Calls the grow method of flower1.
    flower1.bloom() # Calls the bloom method of flower1.
    flower2 = Flower("Daisy" ) # This defines a flower with the name Daisy from the Flower class.
    flower2.grow() # Calls the grow method of flower2.
    flower2.bloom() # Calls the bloom method of flower2.
    flower3 = Flower("Lily") # This defines a flower with the name Lily from the Flower class.
    flower3.grow() # Calls the grow method of flower3.
    flower3.bloom() # Calls the bloom method of flower3.

if __name__ == "__main__": # This calls the main function when the program is executed.
  main()
