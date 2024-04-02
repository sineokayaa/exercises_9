class Point:
    '''
    Class of the points.
    '''

    def __init__(self, position):
        '''
        method for initialisation
        :param position: x and y in a tuple
        '''
        if position is None:
            self.position = (0, 0)
        else:
            self.position = position
        self.x = position[0]
        self.y = position[1]

    def __str__(self):
        '''
        method for string representation
        :return: string with x and y of the point
        '''
        return f'New point: x = {self.x}, y = {self.y}'

    def __repr__(self):
        '''
        method for interactive representation
        :return: string with x and y of the point
        '''
        return self.__str__()

    def get_x(self):
        '''
        method for getting the x
        :return: x
        '''
        return self.x

    def get_y(self):
        '''
        method for getting the y
        :return: y
        :return:
        '''
        return self.y

    def distance(self, other):
        '''
        method for getting the distance between 2 points
        :param other: other point in a tuple
        :return: the distance
        '''
        distance = ((other[0] - self.x) ** 2 + (other[1] - self.y) ** 2) ** 0.5
        return distance

    def sum(self, other):
        '''
        method for summing x and y of 2 points
        :param other: other point in a tuple
        :return: the new point
        '''
        new = Point((self.x + other[0], self.y + other[1]))
        return new


point_1 = Point((1, 9))
print(point_1)
print(point_1.get_x())
print(point_1.distance((1, 2)))
print(point_1.sum((2, 4)))
