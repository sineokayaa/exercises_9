import time
import random


class Not_Sleeping:
    '''
    Class of not sleeping people.
    '''

    def __init__(self):
        '''
        method for initialisation
        '''
        self.sheeps = 0

    def add_sheep(self):
        '''
        method for counting ships every second
        :return: None
        '''
        while True:
            time.sleep(1)
            self.sheeps += 1
            print(self.sheeps)
            return self.sheeps

    def lost(self):
        '''
        method for making person lost his count
        :return: None
        '''
        stop = random.randint(1, 10)  # The number on what that he losts his count.
        n = random.randint(10, 20)  # How many sec it will take for him to fall asleep.
        for _ in range(n):
            self.add_sheep()
            if self.sheeps == stop:
                self.sheeps = 0
                stop = random.randint(1, 10)
                continue

    def get_count_sheeps(self):
        '''
        method for getting the number of sheeps the fall asleep at
        :return: string with the amount of sheeps he fell asleep at
        '''
        return f'On {self.sheeps} sheep he fell asleep.'


pers_1 = Not_Sleeping()

pers_1.lost()
print(pers_1.get_count_sheeps())
