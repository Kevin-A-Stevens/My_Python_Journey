"""
Getters and Setters
Can add a getter and setter after creating a class
"""
from player import Player

kevin = Player("Kevin")

from enemy import Enemy, Troll, Vampire, VampireKing

random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)
#
# random_monster.take_damage(0)
# print(random_monster)
#
# random_monster.take_damage(9)
# print(random_monster)

# ugly_troll = Troll("Pug")
# print("Ugly troll = {}".format(ugly_troll))
#
# another_troll = Troll("ug")
# print("Another Troll = {}".format(another_troll))
# another_troll.take_damage(8)
# print(another_troll)
#
# brother_troll = Troll("urg")
# print("Brother Troll = {}".format(brother_troll))
#
# ugly_troll.grunt()
# another_troll.grunt()
# brother_troll.grunt()
#
# vamp = Vampire("Vlad")
# print(vamp)
# vamp.take_damage(5)
# print(vamp)
#
# print("-" * 40)
# another_troll.take_damage(30)
# print(another_troll)
#
# while vamp._alive:
#     vamp.take_damage(1)
#     print(vamp)

dracula = VampireKing("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)

