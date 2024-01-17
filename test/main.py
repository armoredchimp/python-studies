import random
import pandas as p
import math


first_names = p.read_csv(
    'D:/Python/test/first_names.csv')['FirstName'].tolist()
last_names = p.read_csv('D:/Python/test/last_names.csv')['LastName'].tolist()
metal_names = p.read_csv('D:/Python/test/bm_names.csv')['MetalNameN'].tolist()
metal_names_eng = p.read_csv(
    'D:/Python/test/bm_names.csv')['MetalNameE'].tolist()


class Musician:
    def __init__(self):
        self.RName = f'{random.choice(first_names)} {random.choice(last_names)}'
        self.MName = f'{random.choice(metal_names)}'
        self.Creativity = random.randint(1, 20)
        self.Talent = random.randint(1, 20)
        self.multi_talented = math.floor(
            random.randint(1, 10) * (self.Talent * 0.5))
        print(self.multi_talented)
        if self.multi_talented > 45:
            self.Guitar, self.Bass, self.Drum, self.Vocal = instruments(
                random.randint(2, 4))
        else:
            self.Guitar, self.Bass, self.Drum, self.Vocal = instruments(1)
        self.Performing = random.randint(1, 20)
        self.Paganism = random.randint(1, 99)
        self.Controversy = random.randint(1, 99)
        self.Songwriting = random.randint(1, 99)
        self.Innovation = random.randint(1, 99)
        self.WorkEthic = random.randint(1, 99)
        self.Acumen = random.randint(1, 99)
        self.Resilience = random.randint(1, 99)
        self.Loyalty = random.randint(1, 99)
        self.Multitask = random.randint(1, 99)
        self.Energy = random.randint(1, 99)
        print(f'Name: {self.MName} {self.RName} Creativity: {self.Creativity} Talent: {self.Talent}  Performing: {self.Performing}')
        print(
            f'Guitar: {self.Guitar} Drum: {self.Drum} Bass: {self.Bass} Vocal: {self.Vocal}')


def instruments(number):
    print(f'number:{number}')
    Guitar = random.randint(1, 29)
    Drum = random.randint(1, 29)
    Bass = random.randint(1, 29)
    Vocal = random.randint(1, 29)
    instruments = ['guitar', 'drum', 'bass', 'vocal']
    for n in range(number):
        instruments_played = random.choice(instruments)
        if 'guitar' == instruments_played:
            Guitar = random.randint(30, 99)
        if 'drum' == instruments_played:
            Drum = random.randint(30, 99)
        if 'bass' == instruments_played:
            Bass = random.randint(30, 99)
        if 'vocal' == instruments_played:
            Vocal = random.randint(30, 99)
        instruments.remove(instruments_played)
    return Guitar, Drum, Bass, Vocal


for n in range(1, 10):
    M = Musician()

# class Band:
#     def __init__(self):
