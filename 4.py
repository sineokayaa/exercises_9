class User:
    '''
    Class of not sleeping people.
    '''

    def __init__(self, id, nick_name, first_name, last_name=None, middle_name=None, gender=None):
        '''
        method for initialisation
        :param id: id of the person
        :param nick_name: nickname of the person
        :param first_name: first name of the person
        :param last_name: last name of the person if it's mentioned
        :param middle_name: middle name of the person if it's mentioned
        :param gender: gender if it's mentioned
        '''
        self.id = id
        self.nick_name = nick_name
        self.first_name=first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def __str__(self):
        '''
        method for string representation
        :return: string with the person's information
        '''
        return f'ID:{self.id}, nick_name: {self.nick_name}, first name: {self.first_name}, last name:{self.last_name}, middle_name:{self.middle_name}, gender:{self.gender}'

    def __repr__(self):
        '''
        method for interactive representation
        :return: string with the person's information
        '''
        return self.__str__()

    def update(self,name_upd=None, middle_name_upd=None, id_upd=None):
        '''
        method for changing the info about the user
        :param name_upd: new name if it is mentioned
        :param middle_name_upd: new middle name if it mentioned
        :param id_upd: new if it is mentioned
        :return: None
        '''
        if name_upd is not None:
            self.nick_name = name_upd
        if middle_name_upd is not None:
            self.middle_name = middle_name_upd
        if id_upd is not None:
            self.id = id_upd

pers = User(2034, 'Lana', 'Kira', 'Parker', 'Nana', 'fem')

print(pers)
pers.update(name_upd='Olya')

print(pers)



