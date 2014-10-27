'''
Created on Oct 25, 2014

@author: Tuan
'''
import codecs
import json
import re

from src.algorithm.graph_builder import GraphBuilder
from src.utils.constant import COMMON_VERB_ALPHABET_FILE, VERB_SIMILARITY_FILE, \
    VERBNET_CLASS_INDEX, COMMON_NOUN_ALPHABET_FILE, NOUN_SIMILARITY_FILE, \
    TEST_LABELLED_FILE, TEST_UNLABELLED_FILE, READING_MODE, CODEC, WRITING_MODE
from src.utils.helper import Alphabet


if __name__ == '__main__':
    verb_alphabet_file = COMMON_VERB_ALPHABET_FILE
    verb_similarity_file = VERB_SIMILARITY_FILE
    vn_class_index = VERBNET_CLASS_INDEX
    noun_alphabet_file = COMMON_NOUN_ALPHABET_FILE
    noun_similarity_file = NOUN_SIMILARITY_FILE
    labelled_file = TEST_LABELLED_FILE
    unlabelled_file = TEST_UNLABELLED_FILE
    
    def build_alphabet(input_files, noun_alphabet_file, verb_alphabet_file):
        verb_alphabet = Alphabet()
        noun_alphabet = Alphabet()
        for input_file in input_files:
            with codecs.open(input_file, READING_MODE, CODEC) as file_handler:
                for line in file_handler:
                    tokens = re.split('\t+', line)
                    if len(tokens) >= 2:
                        verb = tokens[0].strip()
                        noun = tokens[1].strip()
                        verb_alphabet.add(verb)
                        noun_alphabet.add(noun)
        with codecs.open(verb_alphabet_file, WRITING_MODE, CODEC) as file_handler:
            json.dump(verb_alphabet.json_dumps(), file_handler)
        with codecs.open(noun_alphabet_file, WRITING_MODE, CODEC) as file_handler:
            json.dump(noun_alphabet.json_dumps(), file_handler)
    
#     build_alphabet([TEST_LABELLED_FILE, TEST_UNLABELLED_FILE], COMMON_NOUN_ALPHABET_FILE, COMMON_VERB_ALPHABET_FILE)
    
    gb = GraphBuilder(verb_alphabet_file, verb_similarity_file,
                      vn_class_index, noun_alphabet_file,
                      noun_similarity_file, labelled_file, unlabelled_file)
    gb.keep_label_connected()
    gb.calclate_right_eigenvectors()
    gb.calculate_probability()
    gb.calculate_labels()