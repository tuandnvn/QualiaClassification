'''
Created on Mar 27, 2014

@author: Tuan
'''
"""
Query constants
Semantics of the following constant keywords should be checked at
http://www.mediawiki.org/wiki/API:Categorymembers.
"""

import os

from src import ROOT_DIRECTORY


READING_MODE = 'r'
WRITING_MODE = 'w'

CODEC = 'utf-8'

DATA_DIRECTORY = os.path.join(ROOT_DIRECTORY, 'data')
VERBNET_DIRECTORY = os.path.join(DATA_DIRECTORY, 'Verbnet 3.2')
VERBNET_CLASS_INDEX = os.path.join(DATA_DIRECTORY, 'verb_net_class_index.dict')
DEPENDENCY_DB = os.path.join(DATA_DIRECTORY, 'dependency_db.db')
VERB_OBJ_FREQ_TEXT_FILE = os.path.join(DATA_DIRECTORY, 'verb_freqs.txt')
VERB_FREQ_DICT_FILE = os.path.join(DATA_DIRECTORY, 'verb_freq.dict')

COMMON_VERB_ALPHABET_FILE = os.path.join(DATA_DIRECTORY, 'verb_alphabet.alp')
COMMON_NOUN_ALPHABET_FILE = os.path.join(DATA_DIRECTORY, 'noun_alphabet.alp')
VERB_NOUN_FREQ_FILE = os.path.join(DATA_DIRECTORY, 'verb_noun_freq.dict')
VERB_SIMILARITY_FILE = os.path.join(DATA_DIRECTORY, 'verb_similarity.dict')
NOUN_SIMILARITY_FILE = os.path.join(DATA_DIRECTORY, 'noun_similarity.dict')

TEST_LABELLED_FILE = os.path.join(DATA_DIRECTORY, 'test_labelled')
TEST_UNLABELLED_FILE = os.path.join(DATA_DIRECTORY, 'test_unlabelled')

NSUBJPASS_LINK = 'nsubjpass'
OBJ_LINK = 'dobj'
SUBJ_LINK = 'nsubj'

BHAT_SIMI = 'bhattacharya'
WN_NOUN_SIMI = 'wordnet_noun'

PAST_PARTICLE_DICT = {'blacktop' : 'blacktopped', 'lay': 'laid', 'leave': 'left', 'get': 'got',
                      'siphon': 'siphoned', 'tail': 'tailed', 'inch': 'inched', 'domesticate': 'domesticated',
                      'embed': 'embedded', 'savor': 'savored', 'balk': 'balked', 'rack': 'racked',
                      'bolt': 'bolted', 'distil': 'distilled', 'apprise': 'apprised', 'con': 'conned',
                      'fuse': 'fused', 'synthesize': 'synthesized', 'entrust': 'entrusted', 'color': 'colored',
                      'advertise': 'advertised', 'halt': 'halted', 'wrap': 'wrapped', 'summon':'summoned',
                      'enclose': 'enclosed', 'drag':  'dragged', 'bind': 'binded', 'favor': 'favored',
                      'ensure': 'ensured', 'find': 'found', 'use': 'used', 'pay': 'paid', 'offer': 'offered'}

VERB_OBJECT_SEED_FILE = 'verb-object-seeds.txt'
VERB_SUBJECT_SEED_FILE = 'verb-subject-seeds.txt'

QUALIA_CLASS_FILE = 'qualia_class.dict'
VERBNET = 'verbnet'