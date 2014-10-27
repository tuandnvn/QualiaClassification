'''
Created on Oct 5, 2014

@author: Tuan
'''
from _collections import defaultdict
import codecs
import json

import en
import nltk

from src.database_interface.database_handler import WordFinder
from src.utils.constant import VERB_FREQ_DICT_FILE, WRITING_MODE, CODEC, \
    VERB_OBJ_FREQ_TEXT_FILE, READING_MODE, OBJ_LINK, DEPENDENCY_DB, \
    NSUBJPASS_LINK, COMMON_VERB_ALPHABET_FILE, COMMON_NOUN_ALPHABET_FILE, \
    VERB_NOUN_FREQ_FILE, PAST_PARTICLE_DICT
from src.utils.helper import Alphabet


if __name__ == '__main__':
    word_finder = WordFinder(DEPENDENCY_DB)
    selected_number = 100
    
    def find_most_frequent_verb(selected_number):
        verb_obj_freq = {}
        with codecs.open(VERB_OBJ_FREQ_TEXT_FILE, READING_MODE, CODEC) as file_handler:
            for line in file_handler:
                verb, obj_freq = line.split(' ')
                verb_obj_freq[verb] = int(obj_freq)
        
        freq_sorted_verb = sorted(verb_obj_freq.keys(), key=lambda a: verb_obj_freq[a])
        
        verb_freq = defaultdict(dict)
        print freq_sorted_verb[-selected_number:]
        for verb in freq_sorted_verb[-selected_number:]:
            verb = str(verb)
            verb_freq[verb][OBJ_LINK] = verb_obj_freq[verb]
            
            try:
                past_particle = en.verb.past_participle(verb)
            except KeyError:
                past_particle = PAST_PARTICLE_DICT[verb]
            row_object = word_finder.collocate_dtype_sum(past_particle, NSUBJPASS_LINK)
            verb_freq[verb][NSUBJPASS_LINK] = row_object['Count']
            print verb + " " + past_particle + " " + str(verb_freq[verb][NSUBJPASS_LINK])
        
        with codecs.open(VERB_FREQ_DICT_FILE, WRITING_MODE, CODEC) as file_handler:
            json.dump(verb_freq, file_handler)
    
    find_most_frequent_verb(selected_number)
    
    
    def find_noun_vectors_of_verbs():
        proportion_threshold = 100
        verb_nouns = defaultdict(set)
        verb_alphabet = Alphabet()
        noun_alphabet = Alphabet()
            
        stopwords = nltk.corpus.stopwords.words('english')
        verb_nouns_freq_tempo = defaultdict(int)
        verb_noun_freq = defaultdict(int)
        
        with codecs.open(VERB_FREQ_DICT_FILE, READING_MODE, CODEC) as file_handler:
            verb_freq = json.load(file_handler)
            
        for verb in verb_freq:
            total_obj_freq = verb_freq[verb][OBJ_LINK]
            total_nsubjpass_freq  = verb_freq[verb][NSUBJPASS_LINK]
            past_particle = en.verb.past_participle(verb)
            for row_object in word_finder.collocate_dtype(past_particle, OBJ_LINK):
                noun = row_object['Word']
                freq = row_object['Count']
                if (not noun in stopwords):
                    if freq*proportion_threshold > total_obj_freq:
                        verb_nouns[verb].add(noun)
                        verb_nouns_freq_tempo[(verb, noun)] += freq
                         
            for row_object in word_finder.collocate_dtype(verb, NSUBJPASS_LINK):
                noun = row_object['Word']
                freq = row_object['Count']
                if (not noun in stopwords):
                    if freq*proportion_threshold > total_nsubjpass_freq:
                        verb_nouns[verb].add(noun)
                        verb_nouns_freq_tempo[(verb, noun)] += freq
            
            verb_alphabet.add(verb)
            verb_index = verb_alphabet.get_index(verb)
            for noun in verb_nouns[verb]:
                if not noun_alphabet.has_label(noun):
                    noun_alphabet.add(noun)
                noun_index = noun_alphabet.get_index(noun)
                verb_noun_freq[(verb_index, noun_index)] = verb_nouns_freq_tempo[(verb, noun)]
            
        with codecs.open(COMMON_VERB_ALPHABET_FILE, WRITING_MODE, CODEC) as file_handler:
            json.dump(verb_alphabet.json_dumps(), file_handler)
            
        with codecs.open(COMMON_NOUN_ALPHABET_FILE, WRITING_MODE, CODEC) as file_handler:
            json.dump(noun_alphabet.json_dumps(), file_handler)
            
        with codecs.open(VERB_NOUN_FREQ_FILE, WRITING_MODE, CODEC) as file_handler:
            json.dump(verb_noun_freq, file_handler)
            
#     find_noun_vectors_of_verbs()
