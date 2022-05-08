"""
Getters and Setters
Can add a getter and setter after creating a class
"""
from player import Player

kevin = Player("Kevin")

print(kevin.name)
print(kevin.lives)
kevin.lives -= 1
print(kevin)

kevin.lives -= 1
print(kevin)

kevin.lives -= 1
print(kevin)

kevin.lives -= 1
print(kevin)

kevin._lives = 9
print(kevin)

kevin.level = 2
print(kevin)

kevin.level += 5
print(kevin)
