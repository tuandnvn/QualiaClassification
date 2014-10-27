'''
Created on Oct 6, 2014

@author: Tuan
'''
import codecs
import json

from src.utils.constant import READING_MODE, CODEC
from src.utils.helper import Alphabet


class WordAlphabet(object):
    def __init__(self, verb_alphabet_file):
        self.alphabet_file = verb_alphabet_file
        with codecs.open(self.alphabet_file, READING_MODE, CODEC) as file_handler:
            self.word_alphabet = Alphabet.json_loads(json.load(file_handler))
    
    def get_index(self, label):
        if  self.word_alphabet.has_label(label.lower()):
            return self.word_alphabet.get_index(label.lower())
        return None
    
    def get_label(self, index):
        return self.word_alphabet.get_label(index)
    
    def size(self):
        return self.word_alphabet.size()