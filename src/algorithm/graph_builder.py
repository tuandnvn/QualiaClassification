'''
Created on Oct 5, 2014

@author: Tuan
'''
from _collections import defaultdict
import codecs
import json
import re

import numpy as np
from src.algorithm.class_alphabet import ClassAlphabet
from src.algorithm.word_alphabet import WordAlphabet
from src.seeding_data.seed_readers import SeedReader
from src.utils.constant import READING_MODE, CODEC
from src.utils.helper import Alphabet
from src.verb_net.verb_vn_similarity import VerbVNSimilarity
from src.word_net.noun_similarity import NounSimilarity


class VN_WN_Metric(object):
    def __init__(self, verb_alphabet_file, verb_similarity_file, vn_class_index,
                 noun_alphabet_file, noun_similarity_file):
        self.verb_metric = VerbVNSimilarity(verb_alphabet_file, verb_similarity_file, vn_class_index)
        self.noun_metric = NounSimilarity(noun_alphabet_file, noun_similarity_file)
        self.verb_weight = float(2) / 3
        self.noun_weight = float(1) / 3
    
    def get_metric_two_nodes(self, node_1, node_2):
        verb_1_index, noun_1_index = node_1
        verb_2_index, noun_2_index = node_2
        verb_distance = self.verb_metric.get_verbnet_similarity(verb_1_index, verb_2_index)
        noun_distance = self.noun_metric.get_wordnet_similarity(noun_1_index, noun_2_index)
        return self.verb_weight * verb_distance + self.noun_weight * noun_distance
        
        
class GraphBuilder(object):
    '''
    '''

    def __init__(self, verb_alphabet_file, verb_similarity_file,
                 vn_class_index, noun_alphabet_file,
                 noun_similarity_file, labelled_file, unlabelled_file):
        '''
        '''
        
        self.number_of_neighbors = 5
        self.verb_alphabet_file = verb_alphabet_file
        self.noun_alphabet_file = noun_alphabet_file
        self.labelled_file = labelled_file
        self.unlabelled_file = unlabelled_file
        self.metric_calculator = VN_WN_Metric(verb_alphabet_file, verb_similarity_file, vn_class_index,
                 noun_alphabet_file, noun_similarity_file)
        self.build_data()
        self.build_nodes()
    
    def build_data(self):
        '''
        The alphabet could be added on the fly
        '''
        self.verb_alphabet = WordAlphabet(self.verb_alphabet_file)
        self.noun_alphabet = WordAlphabet(self.noun_alphabet_file)
        '''
        Fixed alphabet
        '''
        self.class_alphabet = ClassAlphabet()
        
        '''
        unlabelled_verb_nouns store a map of (verb, noun) pair to the frequency seen in google data
        possibly it could just map (verb, noun) pair to 1
        the key of the map will be turned into unlabelled nodes in the graph
        frequency will be ignored
        '''
        with codecs.open(self.unlabelled_file, READING_MODE, CODEC) as file_handler:
            self.unlabelled_verb_nouns = []
            for line in file_handler:
                tokens = re.split('\t+', line)
                if len(tokens) >= 2:
                    verb = tokens[0].strip()
                    noun = tokens[1].strip()
                    verb_index = self.verb_alphabet.get_index(verb)
                    noun_index = self.noun_alphabet.get_index(noun)
                    if verb_index != None and noun_index != None:
                        self.unlabelled_verb_nouns.append((verb_index, noun_index))
                        
        '''
        read back the seed files, 
        '''
        self.seed_reader = SeedReader(self.labelled_file, self.verb_alphabet_file, self.noun_alphabet_file)
        self.labelled_verb_object_dict = self.seed_reader.get_verb_object_dict()
            
    def build_nodes(self):
        self.node_alphabet = Alphabet()
        verb_index_to_noun_indices = defaultdict(list)
        noun_index_to_verb_indices = defaultdict(list)
        self.node_distance_dict = defaultdict(dict)
        
        self.labeled_nodes = defaultdict(dict)
        '''
        Add labelled nodes
        '''
        for verb_index, noun_index in self.labelled_verb_object_dict:
            self.node_alphabet.add((verb_index, noun_index))
            node_index = self.node_alphabet.get_index((verb_index, noun_index))
            qualia_list = self.labelled_verb_object_dict[(verb_index, noun_index)]
            for qualia_index in qualia_list:
                self.labeled_nodes[node_index][qualia_index] = float(1) / len(qualia_list)
            verb_index_to_noun_indices[verb_index].append(noun_index)
            noun_index_to_verb_indices[noun_index].append(verb_index)
        
        '''
        Add unlabelled nodes
        '''        
        for verb_index, noun_index in self.unlabelled_verb_nouns:
            if not self.node_alphabet.has_label((verb_index, noun_index)):
                self.node_alphabet.add((verb_index, noun_index))
            verb_index_to_noun_indices[verb_index].append(noun_index)
            noun_index_to_verb_indices[noun_index].append(verb_index)
        
        for node_index in xrange(self.node_alphabet.size()):
            verb_index, noun_index = self.node_alphabet.get_label(node_index)
#             print str(node_index) + ' ' + self.verb_alphabet.get_label(verb_index) + ' ' + self.noun_alphabet.get_label(noun_index)
        
        for verb_index in verb_index_to_noun_indices:
            for noun_index_1 in verb_index_to_noun_indices[verb_index]:
                for noun_index_2 in verb_index_to_noun_indices[verb_index]:
                    node_1 = (verb_index, noun_index_1)
                    node_2 = (verb_index, noun_index_2)
                    node_index_1 = self.node_alphabet.get_index(node_1)
                    node_index_2 = self.node_alphabet.get_index(node_2)
                    distance = self.metric_calculator.get_metric_two_nodes(node_1, node_2)
                    if not node_index_1 in self.labeled_nodes:
                        self.node_distance_dict[node_index_1][node_index_2] = distance
                     
                    if not node_index_2 in self.labeled_nodes:
                        self.node_distance_dict[node_index_2][node_index_1] = distance
        
        for noun_index in noun_index_to_verb_indices:
            for verb_index_1 in noun_index_to_verb_indices[noun_index]:
                for verb_index_2 in noun_index_to_verb_indices[noun_index]:
                    node_1 = (verb_index_1, noun_index)
                    node_2 = (verb_index_2, noun_index)
                    node_index_1 = self.node_alphabet.get_index(node_1)
                    node_index_2 = self.node_alphabet.get_index(node_2)
                    distance = self.metric_calculator.get_metric_two_nodes(node_1, node_2)
                    if not node_index_1 in self.labeled_nodes:
                        self.node_distance_dict[node_index_1][node_index_2] = distance
                     
                    if not node_index_2 in self.labeled_nodes:
                        self.node_distance_dict[node_index_2][node_index_1] = distance
        
        for noun_index in self.labeled_nodes:
            self.node_distance_dict[noun_index][noun_index] = 1
        
        no_of_nodes = self.node_alphabet.size()
        self.incident_matrix = np.zeros((no_of_nodes, no_of_nodes))
        for node_index in self.node_distance_dict:
            if node_index in self.labeled_nodes:
                self.incident_matrix[node_index, node_index] = 1
            else:
                distance_sorted = sorted(self.node_distance_dict[node_index].keys(), key=lambda a: self.node_distance_dict[node_index][a])
                neighbors = distance_sorted[-self.number_of_neighbors:]
                
                sum_weight = 0
                
                for node_index_2 in neighbors:
                    sum_weight += self.node_distance_dict[node_index][node_index_2]
                for node_index_2 in neighbors:
                    self.incident_matrix[node_index, node_index_2] = float(self.node_distance_dict[node_index][node_index_2]) / sum_weight
#         print self.incident_matrix
        
    def keep_label_connected(self):
        # keep_label_connected = KLC
        visited = set()
        yet_to_be_visited = set(self.labeled_nodes.keys())
        
        while len(yet_to_be_visited) > 0 :
            tempo_yet_to_be_visited = set()
            for node_index in yet_to_be_visited:
                ancestor_node_indices = np.where(self.incident_matrix[:, node_index] > 0)
                tempo_yet_to_be_visited = tempo_yet_to_be_visited.union(set(ancestor_node_indices[0]))
            visited = visited.union(yet_to_be_visited)
            yet_to_be_visited = tempo_yet_to_be_visited.difference(visited)
        
        self.sorted_visited = sorted(list(visited))
        self.sorted_visited_inverted_map = {}
        for i in xrange(len(self.sorted_visited)):
            self.sorted_visited_inverted_map[self.sorted_visited[i]] = i
        
        self.no_of_connected = len(self.sorted_visited)
        self.KLC_node_distance_dict = defaultdict(dict)
        self.KLC_incident_matrix = np.zeros((self.no_of_connected, self.no_of_connected))
        
        for node_index_1 in self.node_distance_dict:
            if node_index_1 in self.sorted_visited_inverted_map:
                KLC_node_index_1 = self.sorted_visited_inverted_map[node_index_1]
                for node_index_2 in self.node_distance_dict[node_index_1]:
                    if node_index_2 in self.sorted_visited_inverted_map:
                        KLC_node_index_2 = self.sorted_visited_inverted_map[node_index_2]
                        self.KLC_node_distance_dict[KLC_node_index_1][KLC_node_index_2] = \
                         self.node_distance_dict[node_index_1][node_index_2]
        
        self.KLC_sparse_index = [] 
        for node_index in self.KLC_node_distance_dict:
            if node_index in self.labeled_nodes:
                self.KLC_incident_matrix[node_index, node_index] = 1
                self.KLC_sparse_index.append((node_index, node_index))
            else:
                distance_sorted = sorted(self.KLC_node_distance_dict[node_index].keys(), key=lambda a: self.KLC_node_distance_dict[node_index][a])
                neighbors = distance_sorted[-self.number_of_neighbors:]
                
                sum_weight = 0
                
                for node_index_2 in neighbors:
                    sum_weight += self.KLC_node_distance_dict[node_index][node_index_2]
                for node_index_2 in neighbors:
                    self.KLC_incident_matrix[node_index, node_index_2] = float(self.KLC_node_distance_dict[node_index][node_index_2]) / sum_weight
                    self.KLC_sparse_index.append((node_index, node_index_2))
        
#         print "=================================================================="
#         print self.KLC_incident_matrix
    
    def calclate_right_eigenvectors(self):
        print '---------------------------calclate-right-eigenvectors--------------------------'
        self.no_of_labeled = len(self.labeled_nodes.keys())
        self.normalized_eigenvectors = []
        for i in xrange(self.no_of_labeled):
            # Find the i'th normalized_eigenvector
            # For each normalized_eigenvector v_i of the form [ 0, 0, ...0, a_i, 0, ... 0, a_l+1, ... a_n ]
            # We have:
            # A = KLC_incident_matrix
            # A * v_i  =  v_i
            # A_modified = removing the first l column and l rows and subtract one from cell (index, index), index >= no_of_labeled 
            # A_modified * v_i_modified = - A[column_i] 
            # v_modified = [ a_l+1, ... a_n ] ( already normalized with a_i == 1 ) 
            # size(A) =    self.no_of_connected x self.no_of_connected
            # size(A_modified) = ( self.no_of_connected - self.no_of_labeled ) x ( self.no_of_connected - self.no_of_labeled )
            # size(v_i_modified) = (self.no_of_connected - self.no_of_labeled ) x 1
            # size(B_vector) = ( self.no_of_connected - self.no_of_labeled ) x 1
            
            matrix_a = np.zeros((self.no_of_connected - self.no_of_labeled, self.no_of_connected - self.no_of_labeled))
            # matrix a is not correctly calculated
            for node_index, node_index_2 in self.KLC_sparse_index:
                if node_index >= self.no_of_labeled and node_index_2 >= self.no_of_labeled:
                    node_index_modified = node_index - self.no_of_labeled
                    node_index_2_modified = node_index_2 - self.no_of_labeled
                
                    if node_index != node_index_2:
                        matrix_a[node_index_modified, node_index_2_modified] = \
                            self.KLC_incident_matrix[node_index, node_index_2]
                    else:
                        # The edge for node_index == node_index_2 (need to subtract 1)
                        matrix_a[node_index_modified, node_index_2_modified] = \
                            self.KLC_incident_matrix[node_index, node_index_2] - 1
#             print "=================================================================="
#             print matrix_a
            
            matrix_b = -self.KLC_incident_matrix[:, i][self.no_of_labeled:]
            
#             print "=================================================================="
#             print matrix_b
            
            modified_eigenvector = np.linalg.lstsq(matrix_a, matrix_b) [0]
            
            print modified_eigenvector
            self.normalized_eigenvectors.append(modified_eigenvector)
            
            original_eigenvector = np.zeros( (self.no_of_connected, 1) )
            original_eigenvector[self.no_of_labeled:, 0] = modified_eigenvector
            original_eigenvector[i] = 1
#             print original_eigenvector
#             print self.KLC_incident_matrix.shape
#             print original_eigenvector.shape
#             print np.dot(self.KLC_incident_matrix, original_eigenvector)
    
    def calculate_probability(self):
        print '------------------------------calculate_probability--------------------------'
        '''
        Calculate according to the formula:
        P(y_n = k)  = Sum ( m is a k labelled node ) v_m_n / v_m_m * prob [m, label]
                    = Sum ( m is a k labelled node ) self.normalized_eigenvectors [m][n] * prob [m, label] 
        '''
        '''
        prob_calculated_unlabeled to store the probability corresponding 
        to a label and a node
        It only store prob for unlabelled nodes
        '''
        self.prob_calculated_unlabeled = np.zeros((self.class_alphabet.size(), self.no_of_connected - self.no_of_labeled))
        self.class_index_eigenvector_matrix = {}
        
        '''
        labeled_inverted invert the labeled_node,
        map from a qualia to the set of nodes
        '''
        self.labeled_inverted = defaultdict(list)
        for node_index in self.labeled_nodes:
            qualia_list = self.labeled_nodes[node_index]
            for qualia_index in qualia_list:
                label_prob = self.labeled_nodes[node_index][qualia_index]
                self.labeled_inverted[qualia_index].append((node_index, label_prob))
        
        '''
        no_of_samples: nodes corresponding to one qualia
        
        '''        
        for qualia_index in xrange(self.class_alphabet.size()):
            no_of_samples = len(self.labeled_inverted[qualia_index])
            self.class_index_eigenvector_matrix[qualia_index] = np.zeros((no_of_samples, self.no_of_connected - self.no_of_labeled))
            for i in xrange(no_of_samples):
                node_index, label_prob = self.labeled_inverted[qualia_index][i]
                self.class_index_eigenvector_matrix[qualia_index][i] = self.normalized_eigenvectors[node_index] * label_prob
            
            self.prob_calculated_unlabeled[qualia_index] = np.sum(self.class_index_eigenvector_matrix[qualia_index], 0)
        print self.prob_calculated_unlabeled
            
    def calculate_labels(self):
        print '--------------------------------calculate_label---------------------------------'
        self.argmax_class_index = np.argmax(self.prob_calculated_unlabeled, 0)
        
        for i in xrange(self.no_of_connected - self.no_of_labeled):
            unlabeled_node_index = self.no_of_labeled + i
            verb_index, noun_index = self.node_alphabet.get_label(unlabeled_node_index)
            verb = self.verb_alphabet.get_label(verb_index)
            noun = self.noun_alphabet.get_label(noun_index)
            print verb + ' ' + noun + ' ' + self.class_alphabet.get_class(self.argmax_class_index[i])