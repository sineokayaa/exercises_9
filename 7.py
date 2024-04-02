class TrafficLight:
    '''
    Class of traffic lights.
    '''
    permissible_values = ['зеленый', 'желтый', 'красный']

    def __init__(self):
        '''
        method for initialisation
        '''
        self.current_signal = 'зеленый'
        self.last = ''

    def __str__(self):
        '''
        method for string representation
        :return: string with the current light signal
        '''
        return f'Light: {self.current_signal}'

    def __repr__(self):
        '''
        method for interactive representation
        :return: string with the current light signal
        '''
        return self.__str__()

    def next_signal(self):
        '''
        method for getting the next signal
        :return: new current signal
        '''
        if self.current_signal == 'зеленый':
            self.last = self.current_signal
            self.current_signal = 'желтый'
            return self.current_signal

        if self.current_signal == 'красный':
            self.last = self.current_signal
            self.current_signal = 'желтый'
            return self.current_signal

        if self.current_signal == 'желтый' and self.last == 'красный':
            self.current_signal = 'зеленый'
            return self.current_signal

        if self.current_signal == 'желтый' and self.last == 'зеленый':
            self.current_signal = 'красный'
            return self.current_signal


now = TrafficLight()

print(now)
now.next_signal()
print(now)
now.next_signal()
print(now)
now.next_signal()
print(now)
now.next_signal()
print(now)
now.next_signal()
print(now)
now.next_signal()
print(now)
now.next_signal()
print(now)
