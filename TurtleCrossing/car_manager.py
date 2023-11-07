from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_ID = 0


class CarManager:
    def __init__(self, player, screen, level):
        self.active = True
        self.level = level
        self.screen = screen
        self.player = player
        self.all_cars = []

    def build_car(self):
        self.car = Car(self.level)
        self.all_cars.append(self.car)

    def move_all_cars(self):
        car_removal = []
        for car in list(self.all_cars):
            if car.move():
                car.move()
                car_removal.append(car)
        for car in car_removal:
            self.all_cars.remove(car)

    def detect_collision(self):
        for car in self.all_cars:
            if (car.collision(self.player, self.screen)):
                # self.player.goto(0, -280)
                self.screen.update()
                collision = True
                return collision

    def clear_all_cars(self):
        for car in self.all_cars:
            for component in car.full_car:
                component.hideturtle()
                component.clear()
        self.all_cars.clear()


class Car:
    def __init__(self, level):
        global CAR_ID, MOVE_INCREMENT
        self.full_car = []
        self.name = CAR_ID
        self.level = level
        self.car_sizes = [1, 2, 3, 4]
        self.car_weights = [1, 49, 1, 1]
        self.cars = random.choices(self.car_sizes, self.car_weights, k=1)[0]
        CAR_ID += 1
        x = 300
        y = random.randint(-210, 270)
        color = random.choice(COLORS)
        for _ in range(self.cars):
            component = CarComponent(x, y, color)
            x += 20
            self.full_car.append(component)

    def move(self):
        out = True
        for component in self.full_car:
            if component.xcor() <= -320:
                component.hideturtle()
                component.clear()
            else:
                new_x, new_y = component.xcor() - (STARTING_MOVE_DISTANCE +
                                                   (MOVE_INCREMENT * self.level * 0.2)), component.ycor()
                component.goto(new_x, new_y)
                out = False
        return out

    def collision(self, player, screen):
        self.player = player
        self.screen = screen
        collided = False
        for component in self.full_car:
            if self.player.distance(component) < 20:
                component.color('black')
                self.screen.update()
                time.sleep(0.5)
                component.color(component.original_color)
                collided = True
        return collided


class CarComponent(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.shape('square')
        self.original_color = color
        self.color(self.original_color)
        self.penup()
        self.goto(x, y)
        self.setheading(180)

    # def buildCar(self):
    #     self.blocks = []
    #     color = random.choice(COLORS)
    #     speed = random.randint(3, 8)
    #     x = 300
    #     y_location = random.randint(-210, 300)
    #     for _ in range(2):
    #         car = Turtle('square')
    #         car.color(f'{color}')
    #         car.penup()
    #         car.goto(x, y_location)
    #         car.pendown()
    #         car.setheading(180)
    #         car.penup()
    #         car.forward(50)
    #         x += 20
    #         self.blocks.append(car)
    #     self.move(self.blocks)

    # def move(car):
    #     self.car = car
    #     new_x, new_y = self.car.xcor()+self.movespeed, self.car.ycor()+self.movespeed
