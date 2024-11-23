import os
import random
import sys
import textwrap
# ATTRIBUTE - ???
class player:
    tempCount = 0
    def __init__(self, weapon, attribute, heal, extra): # ini contractor
        self.weapon = weapon
        self.attribute = attribute
        self.heal = heal
        self.extra = extra
    def display( self ):
        print(f"Weapon : {self.weapon}")
        print(f"Attribute: {self.attribute}")
        print(f"Healing : {self.heal}")
        print(f"Extratation : {self.extra}")
    def Peralatan( self, newWeapon ):
        self.weapon = newWeapon
        
        player.tempCount += 1
        pass
    
class shop:
    def __init__(self, na_weapon):
        self.na_weapon = na_weapon
    def UserWeapon( self ):
        return self.na_weapon
class weapon:
    def __init__(self, na_weapon):
        self.na_weapon = na_weapon
    def UserWeapon( self ):
        return self.na_weapon
class shop:
    def __init__(self, na_sword):
        self.na_sword = na_sword
class armor:
    def __init__(self, na_user):
        self.na_user = na_user
    def UserWeapon( self ):
        return self.na_user

        
TypeWeapon = weapon("Sword")
Weapon = weapon("Shield")
Weapon = armor("Armor")

Weapon = shop("weapon 1")
Weapon2 = shop("Weapon 2")

def main():
    ShopObject = weapon()
    
    print(f"Counted Object : {player.tempCount}")


class shopperkeeper:
    def __init__(shopper):
        print(f"hello there, Would you like to Order some?")
    def __init__(shopper):
        print(f"Which Will You Buy?")
    def __init__ (shopper):
        print(f"So you want to buy {weapon}?")
    def __init__ (shopper):
        print(f"IS there anything would you buy for other?")
    def __init__ (shopper):
        print(f"Alright, thank you!")

def main():
    run = shopperkeeper()

    
if __name__ == "__main__":
    main()
    
