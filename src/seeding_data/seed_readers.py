'''
Created on Oct 6, 2014

@author: Tuan
'''
from _collections import defaultdict
import codecs
import re

from src.algorithm.class_alphabet import ClassAlphabet
from src.algorithm.word_alphabet import WordAlphabet
from src.utils.constant import READING_MODE, CODEC


class SeedReader(object):
    '''
    classdocs
    '''

    def __init__(self, seed_file, verb_alphabet_file, noun_alphabet_file):
        '''
        Constructor
        '''
        self.class_alphabet = ClassAlphabet()
        self.verb_object_dict = defaultdict(list)
        self.seed_file = seed_file
        self.verb_alphabet = WordAlphabet(verb_alphabet_file)
        self.noun_alphabet = WordAlphabet(noun_alphabet_file)
        self.read_seed_file()
    
    def read_seed_file(self):
        with codecs.open(self.seed_file, READING_MODE, CODEC) as file_handler:
            for line in file_handler:
                values = re.split("\t+", line)
                if len(values) >= 3:
                    verb = str(values[0]).strip()
                    noun = str(values[1]).strip()
                    qualias = str(values[2]).strip()
                    verb_index = self.verb_alphabet.get_index(verb)
                    noun_index = self.noun_alphabet.get_index(noun)
                    for qualia in re.split(" ", qualias):
                        qualia_index = self.class_alphabet.get_class_index(qualia)
                        if verb_index != None and noun_index != None and qualia_index != None:
                            self.verb_object_dict[(verb_index, noun_index)].append(qualia_index)
    
    def get_verb_object_dict(self):
        return self.verb_object_dict
