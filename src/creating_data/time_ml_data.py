'''
Created on Oct 22, 2014

@author: Tuan
'''
import codecs
import glob
import os

from src.creating_data import TE3_PLA_ORIGINAL, TE3_PLA_CLEANED
from src.utils.constant import  CODEC, WRITING_MODE, DATA_DIRECTORY
import xml.etree.ElementTree as ET


if __name__ == '__main__':
    all_files = glob.glob(os.path.join(DATA_DIRECTORY, TE3_PLA_ORIGINAL, "*.TE3input.quoted_cleaned"))
    for file_name in all_files:
        print file_name
        result = ''
        parsed = ET.parse(file_name)
        text = parsed.find('TEXT').text
        lines = text.split('\n')
        result = '\n'.join([line for line in lines if line.strip() != ''])
        
        backslash_index = file_name.rfind('\\')
        rel_name = file_name[backslash_index + 1:]
        prefix_rel_name = rel_name[:rel_name.find('.')]
        with codecs.open(os.path.join(DATA_DIRECTORY, TE3_PLA_CLEANED, prefix_rel_name + '.cleaned'), WRITING_MODE, CODEC) as file_handler:
            file_handler.write(result)
