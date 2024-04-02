class Game:
    '''
    Class of basketball players.
    '''

    def __init__(self, commands):
        '''
        method for initialisation
        :param commands: dictionary with the name of the team and it's score
        '''
        self.command = commands

    def __str__(self):
        '''
        method for string representation
        :return: string with the teams
        '''
        return f'Teams: {self.command}'

    def __repr__(self):
        '''
        method for interactive representation
        :return: string with the teams
        '''
        return self.__str__()

    def ball_thrown(self, command, points):
        '''
        method for counting the score
        :param command: what team did through the ball
        :param points: how many points did the get
        :return: None
        '''
        if command == 1:
            self.command[list(self.command.keys())[0]] += points
        if command == 2:
            self.command[list(self.command.keys())[1]] += points

    def get_score(self):
        '''
        method for getting the current score
        :return: tuple with the score
        '''
        return (list(self.command.values())[0], list(self.command.values())[1])

    def get_winner(self):
        '''
        method for finding out who is the winner
        :return: the name of the winner or 'Ничья победила!'
        '''
        if list(self.command.values())[0] > list(self.command.values())[1]:
            return f'{list(self.command.keys())[0]} победили!'
        if list(self.command.values())[0] < list(self.command.values())[1]:
            return f'{list(self.command.keys())[1]} победили!'
        return 'Ничья победила!'


commands = Game({'Легенда': 1, 'Крутыши': 2})
print(commands)
commands.ball_thrown(1, 4)
commands.ball_thrown(2, 3)
commands.ball_thrown(1, 3)
commands.ball_thrown(2, 4)
commands.ball_thrown(1, 4)
print(commands.get_score())
commands.ball_thrown(1, 3)
commands.ball_thrown(2, 6)
print(commands.get_score())
print(commands)
print(commands.get_winner())
