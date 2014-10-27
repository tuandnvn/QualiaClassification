'''
Created on Oct 6, 2014

@author: Tuan
'''
from _collections import defaultdict
import codecs
import glob
import json
import os

from src.utils.constant import VERBNET_DIRECTORY, WRITING_MODE, \
    VERBNET_CLASS_INDEX, CODEC
from src.verb_net.verb_net_reader import VerbNetReader


if __name__ == '__main__':
    verb_class_file_names = glob.glob(os.path.join(VERBNET_DIRECTORY, '*.xml'))
    verb_to_file = defaultdict(list)
    
    for verb_class_file_name in verb_class_file_names:
        print verb_class_file_name
        verb_net_object = VerbNetReader(verb_class_file_name).process_verb_net_file()
        for elements in verb_net_object.findall('.//MEMBERS'):
            for element in elements:
                verb = element.attrib['name']
                verb_to_file[verb].append(verb_class_file_name[verb_class_file_name.rfind(os.path.sep) + 1:])
    with codecs.open(VERBNET_CLASS_INDEX, WRITING_MODE, CODEC) as file_handler:
        json.dump(verb_to_file, file_handler)