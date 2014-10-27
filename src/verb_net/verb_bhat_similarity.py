'''
Created on Oct 25, 2014

@author: Tuan
'''
from _collections import defaultdict
import codecs
import json
import math

import numpy as np
from src.algorithm.word_alphabet import WordAlphabet
from src.utils.constant import READING_MODE, CODEC, WRITING_MODE


class VerbBhatSimilarity(object):
    '''
    classdocs
    '''


    def __init__(self, verb_noun_freq_file, verb_similarity_file, noun_alphabet_file, verb_alphabet_file):
        '''
        Constructor
        '''
        self.verb_noun_freq_file = verb_noun_freq_file
        self.verb_similarity_file = verb_similarity_file
        self.noun_alphabet_file = noun_alphabet_file
        self.verb_alphabet_file = verb_alphabet_file
        self.build_data()
    
    def build_data(self):
        with codecs.open(self.verb_noun_freq_file, READING_MODE, CODEC) as file_handler:
            self.unlabelled_verb_nouns = json.load(file_handler)
            
        self.verb_to_noun_freq_dict = defaultdict(dict)
        for verb_index, noun_index in self.unlabelled_verb_nouns:
            self.verb_to_noun_freq_dict[verb_index][noun_index] = self.unlabelled_verb_nouns((verb_index, noun_index))
        
        self.verb_alphabet = WordAlphabet(self.verb_alphabet_file)
        self.noun_alphabet = WordAlphabet(self.noun_alphabet_file)
        
        with codecs.open(self.verb_similarity_file, READING_MODE, CODEC) as file_handler:
            self.similarity = json.load(file_handler)
    
    def save_data(self):
        with codecs.open(self.verb_similarity_file, WRITING_MODE, CODEC) as file_handler:
            json.dump(self.similarity, file_handler)
            
    def get_bhattacharya_distance(self, verb_1_index, verb_2_index):
        return math.sqrt(1 - self.get_bhattacharya_similarity(verb_1_index, verb_2_index))
    
    def get_bhattacharya_similarity(self, verb_1_index, verb_2_index):
        if (verb_1_index, verb_2_index) in self.similarity:
            return self.similarity[(verb_1_index, verb_2_index)]
        verb_1_vector = np.zeros(self.noun_alphabet.size())
        verb_2_vector = np.zeros(self.noun_alphabet.size())
        for noun_index in self.verb_to_noun_freq_dict[verb_1_index]:
            verb_1_vector[noun_index] = self.verb_to_noun_freq_dict[verb_1_index][noun_index]
        
        for noun_index in self.verb_to_noun_freq_dict[verb_2_index]:
            verb_2_vector[noun_index] = self.verb_to_noun_freq_dict[verb_2_index][noun_index]
        
        verb_1_vector /= np.sum(verb_1_vector)
        verb_2_vector /= np.sum(verb_2_vector)
        similarity = np.sqrt(verb_1_vector * verb_2_vector)
        self.similarity[(verb_1_index, verb_2_index)] = similarity
        return similarity