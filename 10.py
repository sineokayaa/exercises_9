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


class Segment:
    '''
    Class for segments.
    '''

    def __init__(self, point1, point2):
        '''
        method for initialisation
        :param point1: first point
        :param point2: second point
        '''
        self.point1 = point1
        self.point2 = point2
        self.segment = (point1, point2)
        if self.point1[0] > 0 and self.point2[0] > 0 and abs(self.point1[1] + self.point2[1]) <= abs(self.point1[1]):
            self.one_intersection = True
        elif self.point1[1] > 0 and self.point2[1] > 0 and abs(self.point1[0] + self.point2[0]) <= abs(self.point1[0]):
            self.one_intersection = True
        else:
            self.one_intersection = False

    def __str__(self):
        '''
        method for string representation
        :return: ends of segment
        '''
        return (f'Ends of segment : point 1 = {self.point1}, point 2 = {self.point2}, result: {self.one_intersection}')

    def __repr__(self):
        '''
        method for interactive representation
        :return: ends of segment
        '''
        return self.__str__()


class CoordinateSystem:
    '''
    Class of coordinate system
    '''
    segments = []

    def __init__(self, segments):
        '''
        method for initialisation
        :param segments: class attribute with all the segments
        '''
        self.segments.append(segments)

    def __str__(self):
        '''
        method for string representation
        :return: list of all og the segments
        '''
        return f'All segments: {self.segments}'

    def __repr__(self):
        '''
        method for interactive representation
        :return: list of all og the segments
        '''
        return self.__str__()

    def add_segment(self, segment):
        '''
        method for adding new segment to the list
        :param segment: new segment
        :return: None
        '''
        self.segments.append(segment)

    def axis_intersection(self):
        '''
        method for counting segments that cross one of the coordinate axis
        :return: count
        '''
        count = 0
        for i in self.segments:
            exemp = Segment(i[0], i[1])
            if exemp.one_intersection:
                count += 1
        return count


point_1_1 = Point((-1, 2))
point_1_2 = Point((2, -2))
inter_1 = Segment(point_1_1.position, point_1_2.position)
point_2_1 = Point((1, 2))
point_2_2 = Point((1, -2))
inter_2 = Segment(point_2_1.position, point_2_2.position)
point_3_1 = Point((-1, 1))
point_3_2 = Point((1, 2))
inter_3 = Segment(point_3_1.position, point_3_2.position)
res = CoordinateSystem(inter_1.segment)
res.add_segment(inter_2.segment)
res.add_segment(inter_3.segment)
print(res)
print(res.axis_intersection())
