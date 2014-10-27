'''
Created on Oct 25, 2014

@author: Tuan
'''
import codecs
import json

from src.utils.constant import WRITING_MODE, CODEC, READING_MODE


class JsonWrapper(object):
    '''
    wrap json so that 
    it could dump with key of type tuple
    '''

    def __init__(self, separator):
        '''
        Constructor
        '''
        self.separator = separator
    
    def dump(self, dictionary, file_name):
        dict_modified = {}
        for key in dictionary:
            if type(key) == tuple or type(key) == list:
                modified_key = self.separator.join([str(value) for value in key])
                dict_modified[modified_key] = dictionary[key]
        with codecs.open(file_name, WRITING_MODE, CODEC) as file_handler: 
            json.dump(dict_modified, file_handler)
            
    def load(self, file_name):
        with codecs.open(file_name, READING_MODE, CODEC) as file_handler: 
            dict_modified = json.load(file_handler)
        dictionary = {}
        for key in dict_modified:
            modified_key = tuple(key.split(self.separator))
            dictionary[modified_key] = dict_modified[key]
        return dictionary
    
    def load_int_key_tuple(self, file_name):
        with codecs.open(file_name, READING_MODE, CODEC) as file_handler: 
            dict_modified = json.load(file_handler)
        dictionary = {}
        for key in dict_modified:
            modified_key = tuple([int(val) for val in key.split(self.separator)])
            dictionary[modified_key] = dict_modified[key] 
        return dictionary
