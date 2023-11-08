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
        self.all_cars, self.left_cars, self.right_cars = [], [], []

    def build_cars(self):
        right_x, right_y = 320, random.randint(30, 260)
        left_x, left_y = -320, random.randint(-240, -10)
        self.right_car = Car(self.level, right_x, right_y)
        self.left_car = Car(self.level, left_x, left_y)
        self.all_cars.extend([self.right_car, self.left_car])
        self.right_cars.append(self.right_car)
        self.left_cars.append(self.left_car)

    def move_all_cars(self):
        for car in list(self.right_cars):
            if car.move_west():
                self.all_cars.remove(car)
                self.right_cars.remove(car)
        for car in list(self.left_cars):
            if car.move_east():
                self.all_cars.remove(car)
                self.left_cars.remove(car)

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
    def __init__(self, level, x, y):
        global CAR_ID, MOVE_INCREMENT
        self.full_car = []
        self.name = CAR_ID
        self.level = level
        self.car_sizes = [1, 2, 3, 4]
        self.car_weights = [1, 49, 1, 1]
        self.cars = random.choices(self.car_sizes, self.car_weights, k=1)[0]
        self.y = y
        self.x = x
        self.movespeed = STARTING_MOVE_DISTANCE + \
            ((MOVE_INCREMENT + random.randint(-10, 5)) * self.level * 0.2)
        CAR_ID += 1
        # y = random.randint(-210, 270)
        color = random.choice(COLORS)
        for _ in range(self.cars):
            component = CarComponent(x, y, color)
            x += 20
            self.full_car.append(component)

    def move_west(self):
        out = True
        for component in self.full_car:
            if component.xcor() <= -320:
                component.hideturtle()
                component.clear()
            else:
                new_x, new_y = component.xcor() - self.movespeed, component.ycor()
                component.goto(new_x, new_y)
                out = False
        return out

    def move_east(self):
        out = True
        for component in self.full_car:
            if component.xcor() >= 320:
                component.hideturtle()
                component.clear()
            else:
                new_x, new_y = component.xcor() + self.movespeed, component.ycor()
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
        if x > 300:
            self.setheading(180)
        else:
            self.setheading(0)
