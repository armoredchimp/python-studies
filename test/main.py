import random
import pandas as p


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
        self.Performing = random.randint(1, 20)
        self.Paganism = random.randint(1, 99)
        self.Guitar = random.randint(1, 99)
        self.Drum = random.randint(1, 99)
        self.Bass = random.randint(1, 99)
        self.Vocal = random.randint(1, 99)
        self.Controversy = random.randint(1, 99)
        self.Songwriting = random.randint(1, 99)
        self.Innovation = random.randint(1, 99)
        self.WorkEthic = random.randint(1, 99)
        self.Acumen = random.randint(1, 99)
        self.Resilience = random.randint(1, 99)
        self.Loyalty = random.randint(1, 99)
        self.Multitask = random.randint(1, 99)
        self.Energy = random.randint(1, 99)
        print(self.MName, self.RName, self.Creativity,
              self.Talent, self.Performing)


for n in range(1, 10):
    M = Musician()
