'''
Created on Oct 5, 2014

@author: Tuan
'''
import os

from src.utils.constant import VERBNET_DIRECTORY
import xml.etree.ElementTree as ET


class VerbNetReader(object):
    '''
    '''

    def __init__(self, verb_net_file):
        '''
        Constructor
        '''
        self.verb_net_file = verb_net_file
    
    def process_verb_net_file(self):
        tree = ET.parse(self.verb_net_file)
        verb_net_object = tree.getroot()
        return verb_net_object

if __name__=='__main__':
    sample_file = os.path.join(VERBNET_DIRECTORY, 'allow-64.xml')
    verb_net_object = VerbNetReader(sample_file).process_verb_net_file()
    for elements in verb_net_object.findall('.//MEMBERS'):
        for element in elements:
            print element.attrib['grouping']
            print element.attrib['name']
