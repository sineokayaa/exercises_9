class StrandsDNA:
    '''
    Class of strands of the DNA.
    '''
    def __init__(self, all_strands):
        '''
        method for the initialisation
        :param all_strands: the list of DNA-strings
        '''
        self.all_strands = all_strands

    def __str__(self):
        '''
        method for string representation
        :return: string with the current strands
        '''
        return f'Strands: {self.all_strands}'

    def __repr__(self):
        '''
        method for string representation
        :return: string with the current strands
        '''
        return self.__str__()

    def add_strands(self, strands):
        '''
        method for adding a new strand to the list of all strands
        :param strands: string with the strands separated by ' '
        :return: None
        '''
        for i in strands.split():
            self.all_strands.append(i)

    def get_max_strands(self):
        '''
        method for getting the maximum length strands without repetition in lexicographic order
        :return: string with the maximum length strands without repetition in lexicographic order
        '''
        max_length = []
        max_str = ''
        maximum = 0
        for i in self.all_strands:
            if len(i) > maximum:
                maximum = len(i)
        for i in self.all_strands:
            if len(i) == maximum:
                if i not in max_length:
                    max_length.append(i)
        max_length.sort()
        for i in max_length:
            max_str += (i + ' ')
        return max_str

strand = StrandsDNA(['ABC', 'NSD','APS', 'WPEEW', 'ABCDS', 'ABCDS'])
print(strand.get_max_strands())
strand.add_strands('llass dsdasdsl')
print(strand)
print(strand.get_max_strands())