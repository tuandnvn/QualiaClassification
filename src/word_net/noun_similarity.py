'''
Created on Oct 8, 2014

@author: Tuan
'''
import codecs
import json
import math
import os

from nltk.corpus import wordnet

from src.algorithm.word_alphabet import WordAlphabet
from src.utils.constant import READING_MODE, CODEC, \
     WRITING_MODE
from src.utils.json_wrapper import JsonWrapper


class NounSimilarity(object):
    '''
    classdocs
    '''

    def __init__(self, noun_alphabet_file, noun_similarity_file):
        '''
        Constructor
        '''
        self.json_wrapper = JsonWrapper(',')
        self.noun_alphabet_file = noun_alphabet_file
        self.noun_similarity_file = noun_similarity_file
        self.build_data()
        
    def build_data(self):
        self.noun_alphabet = WordAlphabet(self.noun_alphabet_file)
        
        if os.path.isfile(self.noun_similarity_file):
            self.similarity = self.json_wrapper.load_int_key_tuple(self.noun_similarity_file)
        else:
            self.calculate_similarity()
            self.json_wrapper.dump(self.similarity, self.noun_similarity_file)
    
    def calculate_similarity(self):
        for noun_index_1 in xrange(self.noun_alphabet.size()):
            for  noun_index_2 in xrange(self.noun_alphabet.size()):
                self.get_wordnet_similarity(noun_index_1, noun_index_2)
                
    def save_data(self):
        with codecs.open(self.noun_similarity_file, WRITING_MODE, CODEC) as file_handler:
            json.dump(self.similarity, file_handler)
    
    def get_wordnet_distance(self, noun_1_index, noun_2_index):
        return math.pow(1 - self.get_wordnet_similarity(noun_1_index, noun_2_index), 0.5)
    
    def get_wordnet_similarity(self, noun_1_index, noun_2_index):
        if not 'similarity' in self.__dict__:
            self.similarity = {}
        if (noun_1_index, noun_2_index) in self.similarity:
            return self.similarity[(noun_1_index, noun_2_index)]
        
        noun_1 = self.noun_alphabet.get_label(noun_1_index)
        noun_2 = self.noun_alphabet.get_label(noun_2_index)
        noun_1_synsets = wordnet.synsets(noun_1)
        noun_2_synsets = wordnet.synsets(noun_2)
        if len(noun_1_synsets) > 0 and len(noun_2_synsets) > 0 :
            noun_1_main_synset = noun_1_synsets[0]
            noun_2_main_synset = noun_2_synsets[0]
            similarity = round(noun_1_main_synset.wup_similarity(noun_2_main_synset), 3)
        else:
            similarity = 0
        
        self.similarity[(noun_1_index, noun_2_index)] = similarity
        return similarity
        
