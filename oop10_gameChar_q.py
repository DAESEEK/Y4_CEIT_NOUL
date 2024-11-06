#Udon, who works for Nexon, Korea's largest online game company, 
# recently joined a new project, 'Bank Story', as a developer. 
# Udon's part is writing the game characters into 'classes'. 
# We have already thought about the properties and behavior of the object.
# Write the GameCharacter class according to the following conditions 
#                                                                and output examples.

class GameCharacter:
    # game character class
    def __init__(self, name, hp, power):
        d# Game characters have names, hp, and attack power as attributes.

    def is_alive(self):
        d# Method to check if game character is alive (health is over 0)

    def get_attacked(self, damage):
        d
        """
        If the game character is alive, a method that reduces physical strength 
        equal to the attacking character's attack power

         condition:
             1. If the character is already dead, a message saying that the character is dead is displayed.
             2. If the attack power is greater than the remaining HP, the HP becomes 0.
        """

    def attack(self, other_character):
        d# If the game character is alive, 
        # it reduces the physical strength of other characters received 
        # as parameters by the amount of attack power of the character.

    def __str__(self):
        d# Returns a string containing meaningful information about the game character

# Create game character instance                      
character_1 = GameCharacter("WwRambowW", 200, 30)
character_2 = GameCharacter("XxBestKillerxX", 100, 50)

# Game character instances attack each other
character_1.attack(character_2)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)

# output game character instance
print(character_1)
print(character_2)