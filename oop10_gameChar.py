#   Udon, who works for Nexon, Korea's largest online game company, 
# recently joined a new project, 'Bank Story', as a developer. 
# Udon's part is writing the game characters into 'classes'. 
# We have already thought about the properties and behavior of the object.
# Write the GameCharacter class according to the following conditions and output examples.

class GameCharacter:
    # game character class
    def __init__(self, name, hp, power):
         self.name=name
         self.hp=hp
         self.power=power
      
    def is_alive(self):
         return self.hp>0

    def get_attacked(self, damage):
        """
        If the game character is alive, a method that reduces physical strength 
        equal to the attacking character's attack power

         condition:
             1. If the character is already dead, a message saying that the character is dead is displayed.
             2. If the attack power is greater than the remaining HP, the HP becomes 0.
        """
        if self.is_alive:
             self.hp=self.hp-damage if self.hp >= damage else 0
        else:
             print("{} is already dead".format(self.neme))
             
    def attack(self, other_character):
        # If the game character is alive, 
        # it reduces the physical strength of other characters received 
        # as parameters by the amount of attack power of the character.
        if self.is_alive():
             other_character.get_attacked(self.power)
                  
    def __str__(self):
        return self.name+"'s hp remain"+str(self.hp)
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