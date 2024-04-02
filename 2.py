import time


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


pers_1 = Not_Sleeping()

pers_1.add_sheep()
