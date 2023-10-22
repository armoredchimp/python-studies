import snake_file as sf
import food
import random


class Game:
    def __init__(self):
        self.active = False
        self.score = 0
        self.food_coords = [0, 0]
        self.current_food = None
        self.printed = False

    def new_game(self, screen):
        new_snake = sf.Snake(self)
        new_snake.create(4)
        self.active = True
        self.create_food(new_snake)
        while self.active == True:
            new_snake.move()
            if not self.active:
                break
            screen.onkey(key="a", fun=new_snake.turn_left)
            screen.onkey(key="d", fun=new_snake.turn_right)

    def create_food(self, snake):
        x_avg, y_avg = snake.avg_coords()
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        if (x-50 > x_avg or x + 50 < x_avg) and (y-50 > y_avg or y + 50 < y_avg):
            if self.current_food:
                self.current_food.clear()
            morsel = food.Food(x, y)
            self.food_coords = [x, y]
            self.current_food = morsel
        else:
            self.create_food(snake)

    def add_point(self):
        self.score += 1

    def print_score(self):
        if not self.printed:
            print(self.score)
            self.printed = True


game = Game()
game.new_game(sf.screen)

sf.screen.exitonclick()
