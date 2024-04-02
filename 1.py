class Dog:
    '''
    Class of dogs.
    '''
    def __init__(self, name):
        '''
        method for initialisation
        :param name: name of the dog
        '''
        self.name = name

    def __str__(self):
        '''
        method for string representation
        :return: string with the dog's name
        '''
        return f'Имя собаки: {self.name}'

    def __repr__(self):
        '''
        method for interactive representation
        :return: string with the dog's name
        '''
        return self.__str__()



    def say(self):
        '''
        method for barking
        :return: None
        '''
        print('Гав!')


dog = Dog('Dog')
dog.say()
