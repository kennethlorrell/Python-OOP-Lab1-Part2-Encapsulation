import re
from collections import Counter

class TextStat:
    def __init__(self, path, encoding):
        def par_count():
            return len(re.split('\n', self.data))

        def sent_count():    
            return len(re.split('.!?', self.data))

        def word_count():
            return len(re.split('[\s\.\?\,\;\:\!]', self.data))

        def word_freq():
            return Counter(re.split('[\s\.\?\,\;\:\!]', self.data)) 

        def char_count():
            return len(re.split('', self.data))

        def char_freq():
            return Counter(re.split('', self.data))

        with open(path, mode='r', encoding=encoding) as f:
            data = f.read()
        self.name = ''.join(path.split('.')[:-1])
        self.data = data

        self.__par_count = par_count()
        self.__sent_count = sent_count()
        self.__word_count = word_count()
        self.__word_freq = word_freq()
        self.__char_count = char_count()
        self.__char_freq = char_freq()

    def  get_par_count(self):
        return self.__par_count
    
    def  get_sent_count(self):
        return self.__sent_count
    
    def  get_word_count(self):
        return self.__word_count
    
    def  get_word_freq(self):
        return self.__word_freq
        
    def  get_char_count(self):
        return self.__char_count
        
    def  get_char_freq(self):
        return self.__char_freq
