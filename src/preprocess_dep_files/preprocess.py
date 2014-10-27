'''
Created on Oct 26, 2014

@author: User
'''
import codecs
import glob
import os
import re
from string import Formatter

from src.preprocess_dep_files import DEPENDENCY_MASC
from src.utils.constant import READING_MODE, CODEC, DATA_DIRECTORY, WRITING_MODE
from src.utils.helper import Alphabet


class Dependency_Structure(object):
    def __init__(self, sent_no, token_no, token, normalized_token, POS, semantic, head, rel, additional):
        '''
        sent_no should start from 0 
        token_no should start from 1 (root is actually considered first token in a sentence)
        
        1            December        december            NNP        sem=TMP        0        root        _
        token_no    token            normalized_token    POS        semantic        head    rel        additional
        '''
        self.sent_no = int(sent_no)
        self.token_no = int(token_no)
        self.token = token
        self.normalized_token = normalized_token
        self.POS = POS
        self.semantic = semantic
        self.head = head
        self.rel = rel
        self.additional = additional
        self.start = None
        self.end = None
        self.id = None
    
    def __str__(self):
        return str(self.sent_no) + " " + str(self.token_no) + " " + self.token + " " + self.normalized_token + " " + self.POS + " " + self.semantic + " " + self.head + " " + self.rel + " " + self.additional
    
    def __hash__(self):
        val = 1
        prime = 31
        val = prime * val + self.sent_no 
        val = prime * val + self.token_no 
        return val

    def __cmp__(self, other):
        if self.sent_no < other.sent_no:
            return -1
        if self.sent_no > other.sent_no:
            return 1
        if self.token_no < other.token_no:
            return -1
        if self.token_no > other.token_no:
            return 1
        return 0

    def __eq__(self, rhs):
        if self.__cmp__(rhs) == 0:
            return True
        return False
        
def preprocess_dep_file_to_mae_files(input_folder, output_folder):
    dependency_file_names = glob.glob(os.path.join(input_folder, '*.mrg.dep'))
    for dependency_file_name in dependency_file_names:
        def read_input_file(dependency_file_name):
            print("========== Read " + dependency_file_name)
            document_tokens = []
            with codecs.open(dependency_file_name, READING_MODE, CODEC) as file_handler:
                sentence_tokens = []
                line_index = 0
                for line in file_handler:
                    if line.strip() == '':
                        document_tokens.append(sentence_tokens)
                        sentence_tokens = []
                    else:
                        tokens = [token.strip() for token in re.split('\t', line)]
                        token_structure = Dependency_Structure(line_index, *tokens)
                        sentence_tokens.append(token_structure)
                    line_index += 1
            return document_tokens
        
        document_tokens = read_input_file(dependency_file_name)
        
        def write_output_file(document_tokens, mae_file_name):
            print("========== Write " + mae_file_name)
            with codecs.open(mae_file_name, WRITING_MODE, CODEC) as file_handler:
                '''
                <?xml version="1.0" encoding="UTF-8" ?>
                <PartML>
                <TEXT><![CDATA[
                ...
                ]]></TEXT>
                <TAGS>
                <SELECTOR id="s1" start="278" end="282" text="fill" comment="" pos="VERB" />
                <SELECTOR id="s2" start="297" end="303" text="search" comment="" pos="ADJ" />
                ...
                <NOUN id="n1" start="287" end="291" text="void" comment="" />
                <NOUN id="n2" start="304" end="309" text="giant" comment="" />
                ...
                <QLINK id="q0" fromID="s1" fromText="fill" toID="n1" toText="void" comment="" qType="" qType2="" gramRel="" />
                <QLINK id="q1" fromID="n2" fromText="giant" toID="s2" toText="search" comment="" qType="" qType2="" gramRel="" />
                ...
                </TAGS>
                </PartML>
                '''
                text = ''
                length = 1
                relation_included = ['dobj', 'iobj', 'nsubjpass']
                
                verb_nouns = []
                verb_alphabet = Alphabet()
                noun_alphabet = Alphabet()
                for sentence_tokens in document_tokens:
                    for token_structure in sentence_tokens:
                        token = token_structure.token
                        token_structure.start = length
                        token_structure.end = length + len(token)
                        if token_structure.rel in relation_included:
                            # Add into alphabets
                            head_rel_index = int(token_structure.head) - 1
#                             print(sentence_tokens[head_rel_index])
#                             print(token_structure)
                            verb_alphabet.add(sentence_tokens[head_rel_index])
                            sentence_tokens[head_rel_index].id = verb_alphabet.get_index(sentence_tokens[head_rel_index])
                            noun_alphabet.add(token_structure)
                            token_structure.id = noun_alphabet.get_index(token_structure)
                            
                            verb_nouns.append((sentence_tokens[head_rel_index].id, token_structure.id, token_structure.rel))
                        text += token + ' '
                        length += len(token) + 1
                    text += '\n'
                    length += 1
                file_handler.write('<?xml version="1.0" encoding="UTF-8" ?>')
                file_handler.write('\n')
                file_handler.write('<PartML>')
                file_handler.write('\n')
                file_handler.write('<TEXT><![CDATA[')
                file_handler.write('\n')
                file_handler.write(text)
                file_handler.write(']]></TEXT>')
                file_handler.write('\n')
                file_handler.write('<TAGS>')
                file_handler.write('\n')
                formatter = Formatter()
                for verb_structure_index in range(verb_alphabet.size()):
                    verb_structure = verb_alphabet.get_label(verb_structure_index)
                    file_handler.write(formatter.format('<SELECTOR id="s{0.id}" start="{0.start}" end="{0.end}" text="{0.token}" comment="" pos="{0.POS}" />',
                                                        verb_structure))
                    file_handler.write('\n')
                
                for noun_structure_index in range(noun_alphabet.size()):
                    noun_structure = noun_alphabet.get_label(noun_structure_index)
                    file_handler.write(formatter.format('<NOUN id="n{0.id}" start="{0.start}" end="{0.end}" text="{0.token}" comment="" />',
                                                        noun_structure))
                    file_handler.write('\n')
                    
                for index in range(len(verb_nouns)):
                    verb_structure_index, noun_structure_index, rel = verb_nouns[index]
                    verb_structure = verb_alphabet.get_label(verb_structure_index)
                    noun_structure = noun_alphabet.get_label(noun_structure_index)
                    file_handler.write(formatter.format('<QLINK id="q{0}" fromID="s{1.id}" fromText="{1.token}" toID="n{2.id}" toText="{2.token}" comment="" qType="{3}" qType2="" gramRel="{4}" />',
                                                        index,
                                                        verb_structure,
                                                        noun_structure,
                                                        'FORMAL', rel))
                    file_handler.write('\n')
                    
                file_handler.write('</TAGS>')
                file_handler.write('\n')
                file_handler.write('</PartML>')
                file_handler.write('\n')
        
        rel_file_name = dependency_file_name[dependency_file_name.rfind(os.path.sep) + 1:]
        mae_file_name = os.path.join(output_folder, rel_file_name + '.mae')
        write_output_file(document_tokens, mae_file_name)
                    
if __name__ == '__main__':
    preprocess_dep_file_to_mae_files(os.path.join(DATA_DIRECTORY, 'dependency_nltk'), os.path.join(DATA_DIRECTORY, 'dependency_nltk_output'))
    
                
