'''
Created on Oct 5, 2014

@author: Tuan
'''

import glob
import os

from src.database_interface.database_handler import WordFinder
from src.utils.constant import DEPENDENCY_DB, VERBNET_DIRECTORY, OBJ_LINK
from src.verb_net.verb_net_reader import VerbNetReader


if __name__=='__main__':
    verb_class_file_names = glob.glob(os.path.join(VERBNET_DIRECTORY, '*.xml'))
    
    main_sense_verbs = []
    for verb_class_file_name in verb_class_file_names:
        print verb_class_file_name
        verb_net_object = VerbNetReader(verb_class_file_name).process_verb_net_file()
        for elements in verb_net_object.findall('.//MEMBERS'):
            for element in elements:
                is_main_sense = True
                try:
                    groupings = element.attrib['grouping'].split(' ')
                    if len(groupings) > 0:
                        has_main = False
                        for grouping in groupings:
                            if grouping.endswith("01"):
                                has_main = True
                                break
                        if not has_main:
                            is_main_sense = False
                except KeyError:
                    pass
                if is_main_sense:
                    main_sense_verbs.append(element.attrib['name'])
    
    print 'Number of main sense verbs : ' + str(len(main_sense_verbs))
    word_finder = WordFinder(DEPENDENCY_DB)
    
    verb_freq = {}
    
    begin = False
    for verb in main_sense_verbs:
        if begin:
            row_object = word_finder.collocate_dtype_sum(verb, OBJ_LINK)
            verb_freq[verb] = row_object['Count']
            print verb + " " + str(verb_freq[verb])
        if verb == 'count':
            begin = True
