'''
Created on Oct 6, 2014

@author: Tuan
'''
import codecs
import json
import os

from src.utils.constant import QUALIA_CLASS_FILE, WRITING_MODE, CODEC, \
    READING_MODE
from src.utils.helper import Alphabet


class ClassAlphabet(object):
    def __init__(self):
        if os.path.isfile(QUALIA_CLASS_FILE):
            with codecs.open(QUALIA_CLASS_FILE, READING_MODE, CODEC) as file_handler:
                self.class_alphabet = Alphabet.json_loads(json.load(file_handler))
        else:
            ClassAlphabet.initiate_alphabet()
    
    def size(self):
        return self.class_alphabet.num_labels
    
    def get_class_index(self, label_str):
        if self.class_alphabet.has_label(label_str.lower()):
            return self.class_alphabet.get_index(label_str.lower())
        return None
    
    def get_class(self, class_index):
        return self.class_alphabet.get_label(class_index)
    
    @classmethod
    def initiate_alphabet(cls):
        class_alphabet = Alphabet()
        class_alphabet.add('formal')
        class_alphabet.add('telic')
        class_alphabet.add('agentive')
        class_alphabet.add('constitutive')
        with codecs.open(QUALIA_CLASS_FILE, WRITING_MODE, CODEC) as file_handler:
            json.dump(class_alphabet.json_dumps(), file_handler)