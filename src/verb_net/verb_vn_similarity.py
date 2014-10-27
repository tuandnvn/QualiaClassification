'''
Created on Oct 6, 2014

@author: Tuan
'''
import codecs
import json
import os

from src.algorithm.word_alphabet import WordAlphabet
from src.utils.constant import READING_MODE, CODEC, WRITING_MODE
from src.utils.json_wrapper import JsonWrapper


class VerbVNSimilarity(object):
    '''
    classdocs
    '''

    def __init__(self, verb_alphabet_file, verb_similarity_file, vn_class_index):
        '''
        Constructor
        '''
        self.json_wrapper = JsonWrapper(',')
        self.verb_similarity_file = verb_similarity_file
        self.verb_alphabet_file = verb_alphabet_file
        self.vn_class_index = vn_class_index
        self.SAME_VN_CLASS_VAL = 0.8
        self.build_data()
    
    def build_data(self):
        self.verb_alphabet = WordAlphabet(self.verb_alphabet_file)
        with codecs.open(self.vn_class_index, READING_MODE, CODEC) as file_handler:
            self.verb_to_file = json.load(file_handler)
            
        if os.path.isfile(self.verb_similarity_file):
            self.similarity = self.json_wrapper.load_int_key_tuple(self.verb_similarity_file)
        else:
            self.calculate_similarity()
            self.json_wrapper.dump(self.similarity, self.verb_similarity_file)
            
    def calculate_similarity(self):
        for verb_index_1 in xrange(self.verb_alphabet.size()):
            for verb_index_2 in xrange(self.verb_alphabet.size()):
                self.get_verbnet_similarity(verb_index_1, verb_index_2)
    
    def save_data(self):
        with codecs.open(self.verb_similarity_file, WRITING_MODE, CODEC) as file_handler:
            json.dump(self.similarity, file_handler)
    
    def get_verbnet_distance(self, verb_1_index, verb_2_index):
        return (2 - self.get_verbnet_similarity(verb_1_index, verb_2_index)) ^ 2
    
    def get_verbnet_similarity(self, verb_1_index, verb_2_index):
        if not 'similarity' in self.__dict__:
            self.similarity = {}
        if (verb_1_index, verb_2_index) in self.similarity:
            return self.similarity[(verb_1_index, verb_2_index)]
        if verb_1_index == verb_2_index:
            self.similarity[(verb_1_index, verb_2_index)] = 1
        else:
            verb_1 = self.verb_alphabet.get_label(verb_1_index)
            verb_2 = self.verb_alphabet.get_label(verb_2_index)
            verb_class_1_set = set(self.verb_to_file[verb_1])
            verb_class_2_set = set(self.verb_to_file[verb_2])
            print verb_class_1_set
            print verb_class_2_set
            if len(verb_class_1_set.intersection(verb_class_2_set)) > 0:
                self.similarity[(verb_1_index, verb_2_index)] = self.SAME_VN_CLASS_VAL
            else:
                self.similarity[(verb_1_index, verb_2_index)] = 0
        return self.similarity[(verb_1_index, verb_2_index)]
