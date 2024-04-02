class MorseMsg:
    '''
    Class of Morse messages.
    '''
    morse_eng = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                 '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                 '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                 '-.--': 'Y', '--..': 'Z'}
    morse_ru = {'.-': 'А', '-...': 'Б', '.--': 'В', '--.': 'Г', '-..': 'Д', '.': 'Е', '...-': 'Ж', '--..': 'З',
                '..': 'И', '.---': 'Й', '-.-': 'К', '.-..': 'Л', '--': 'М', '-.': 'Н', '---': 'О', '.--.': 'П',
                '.-.': 'Р', '...': 'С', '-': 'Т', '..-': 'У', '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц', '---.': 'Ч',
                '----': 'Ш', '--.-': 'Щ', '-.--': 'Ы', '-..-': 'Ь', '..-..': 'Э', '..--': 'Ю', '.-.-': 'Я'}
    vowels_eng = ['A', 'E', 'I', 'O', 'U', 'Y']
    vowels_ru = ['А', 'О', 'У', 'Ы', 'Э', 'Е', 'Ё', 'И', 'Ю', 'Я']

    def __init__(self, string_m):
        '''
        method for initialisation
        :param string_m: Morse message
        '''
        self.string_m = string_m.split()

    def __str__(self):
        '''
        method for string representation
        :return: string with the Morse message
        '''
        return f'Your text: {self.string_m}'

    def __repr__(self):
        '''
        method for interactive representation
        :return: string with the Morse message
        '''
        return self.__str__()

    def eng_decode(self):
        '''
        method for encoding from Morse to eng letters
        :return: encoded message
        '''
        result_eng = ''
        for i in self.string_m:
            result_eng += self.morse_eng[i]
        return result_eng

    def ru_decode(self):
        '''
        method for encoding from Morse to ru letters
        :return: encoded message
        '''
        result_ru = ''
        for i in self.string_m:
            result_ru += self.morse_ru[i]
        return result_ru

    def get_wowels(self, lang):
        '''
        method for getting only vowels from the encoded message
        :param lang: the language of the vowels
        :return: string with the vowels
        '''
        if lang == 'ru':
            vowels = []
            for i in self.string_m:
                letter =  self.morse_ru[i]
                if letter in self.vowels_ru:
                    vowels.append(self.morse_ru[i])
            return vowels
        if lang == 'eng':
            vowels = []
            for i in self.string_m:
                letter = self.morse_eng[i]
                if letter in self.vowels_eng:
                    vowels.append(self.morse_eng[i])
            return vowels
    def get_consonants(self, lang):
        '''
        method for getting only consonants from the encoded message
        :param lang: the language of the consonants
        :return: string with the consonants
        '''
        if lang == 'ru':
            consonants = []
            for i in self.string_m:
                letter = self.morse_ru[i]
                if letter not in self.vowels_ru:
                    consonants.append(self.morse_ru[i])
            return consonants
        if lang == 'eng':
            consonants = []
            for i in self.string_m:
                letter = self.morse_eng[i]
                if letter not in self.vowels_eng:
                    consonants.append(self.morse_eng[i])
            return consonants


txt = MorseMsg('.--.  .-.  ..  .--  .  -')
print(txt.ru_decode())
print(txt.eng_decode())
print(txt.get_wowels('ru'))
print(txt.get_wowels('eng'))
print(txt.get_consonants('ru'))
print(txt.get_consonants('eng'))



