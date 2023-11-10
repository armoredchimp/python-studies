import snake_file as sf
import food
import random
import time
import scoreboard as sb


class Game:
    def __init__(self):
        self.active = False
        self.score = 0
        self.scoreNum = sb.DynamicScore(self.score)
        self.food_coords = [0, 0]
        self.current_food = None
        self.printed = False

    def new_game(self, screen):
        new_snake = sf.Snake(self)
        new_snake.create(4)
        self.active = True
        scoreboard = sb.StaticBoard()
        self.create_food()
        while self.active == True:
            new_snake.move()
            if not self.active:
                break
            screen.onkey(key="a", fun=new_snake.turn_left)
            screen.onkey(key="d", fun=new_snake.turn_right)

    def create_food(self):

        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        if self.current_food:
            self.current_food.clear()
        morsel = food.Food(x, y)
        self.food_coords = [x, y]
        self.current_food = morsel

    def add_point(self):
        temp = self.score + 1
        self.scoreNum.clear()
        self.scoreNum = sb.DynamicScore(temp)
        self.score = temp

    def print_score(self):
        if not self.printed:
            gmov = sb.GameOver(self.score)
            self.printed = True
            if self.current_food:
                self.current_food.clear()
            sf.screen.update()
            time.sleep(3)
            self.scoreNum.clear()
            gmov.clear()
            new_game = Game()
            new_game.new_game(sf.screen)


game = Game()
game.new_game(sf.screen)

sf.screen.exitonclick()
