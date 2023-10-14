import alt_module
import prettytable

# import turtle
# from turtle import Turtle, Screen

# print(alt_module.secret)


# timmy = Turtle()

# print(timmy)
# timmy.shape("turtle")
# timmy.color("chocolate")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ['Pokemon Name', 'Type']
table.add_row(['Pikachu', 'Electric'])
table.add_row(['Squirtle', 'Water'])
table.add_row(['Charmander', 'Fire'])
# table.align['Pokemon Name'] = "l"
# table.align['Type'] = "l"
table.align = 'l'
print(table)
