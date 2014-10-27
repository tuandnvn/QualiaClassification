'''
Created on Sep 29, 2014

@author: Tuan
'''
import sqlite3
import nltk

class WordFinder(object):

    def __init__(self, db_file):
        self.cur = sqlite3.connect(db_file)
        self.cur.row_factory = sqlite3.Row

    def collocate_dtype(self, word, dtype):
        word = word.lower()
        sql_command =   """ SELECT W2.Word AS Word, SUM(D.Count) AS Count
                            FROM DependencyRelations as D, Words as W, Words as W2
                            WHERE W.Word = "%s" AND W2.DepType = "%s" AND 
                            W.WID = D.GovernorID AND W2.WID = D.DependentID 
                            GROUP BY W2.Word
                            ORDER BY SUM(D.Count) DESC
                        """     % (word, dtype)
        results = self.cur.execute(sql_command).fetchall()
        return results
    
    def collocate_dtype_sum(self, word, dtype):
        word = word.lower()
        sql_command =   """ SELECT COUNT(*) AS Count
                            FROM DependencyRelations as D, Words as W, Words as W2
                            WHERE W.Word = "%s" AND W2.DepType = "%s" AND 
                            W.WID = D.GovernorID AND W2.WID = D.DependentID 
                        """     % (word, dtype)
        result = self.cur.execute(sql_command).fetchone()
        return result

    def collocate_head_dtype(self, word, dtype):
        word = word.lower()
        sql_command =   """ SELECT W2.Word as Word, SUM(D.Count) as Count
                            FROM DependencyRelations as D, Words as W, Words as W2
                            WHERE W.Word = "%s" AND W.DepType = "%s" AND 
                            W.WID = D.DependentID AND W2.WID = D.GovernorID
                            GROUP BY W2.Word
                            ORDER BY SUM(D.Count) DESC
                        """     % (word, dtype)
        results = self.cur.execute(sql_command).fetchall()
        return results
    
    def some_word(self, word):
        sql_command = """SELECT * from Words where Word = "%s" """ % word
        results = self.cur.execute(sql_command).fetchall()
        return results

if __name__ == '__main__':
    stopwords = nltk.corpus.stopwords.words('english')
    word_finder= WordFinder('dependency_db.db')
#     for row_object in word_finder.collocate_dtype('eat', 'nsubjpass'):
#             print row_object['Word'] + ' ' + str(row_object['Count'])
    
#     artifact_noun = 'system'
#     print "============nsubjpass============"
#     for row_object in word_finder.collocate_head_dtype(artifact_noun, 'nsubjpass'):
#         print row_object['Word'] + ' ' + str(row_object['Count'])
#     
#     print "============nsubj============"       
#     for row_object in word_finder.collocate_head_dtype(artifact_noun, 'nsubj'):
#         print row_object['Word'] + ' ' + str(row_object['Count'])
#     
#     print "============dobj============"      
#     for row_object in word_finder.collocate_head_dtype(artifact_noun, 'dobj'):
#         print row_object['Word'] + ' ' + str(row_object['Count'])
    
    original_verb = 'bake'
    verb = 'baked'
    print "============nsubjpass============"
    for row_object in word_finder.collocate_dtype(verb, 'nsubjpass')[:30]:
        if (not row_object['Word'] in stopwords):
            print original_verb + '\word_finder' + row_object['Word'] + '\word_finder' + str(row_object['Count'])
    
    verb = 'bake'
    print "============nsubj============"
    for row_object in word_finder.collocate_dtype(verb, 'nsubj')[:40]:
        if (not row_object['Word'] in stopwords):
            print original_verb + '\word_finder' + row_object['Word'] + '\word_finder' + str(row_object['Count'])
    
    print "============dobj============"
    for row_object in word_finder.collocate_dtype(verb, 'dobj')[:20]:
        if (not row_object['Word'] in stopwords):
            print original_verb + '\word_finder' + row_object['Word'] + '\word_finder' + str(row_object['Count'])
            
    verb = 'baked'
    print "============nsubj============"
    for row_object in word_finder.collocate_dtype(verb, 'nsubj')[:40]:
        if (not row_object['Word'] in stopwords):
            print original_verb + '\word_finder' + row_object['Word'] + '\word_finder' + str(row_object['Count'])
    
    print "============dobj============"
    for row_object in word_finder.collocate_dtype(verb, 'dobj')[:20]:
        if (not row_object['Word'] in stopwords):
            print original_verb + '\word_finder' + row_object['Word'] + '\word_finder' + str(row_object['Count'])
#     count = 0
#     for row_object in word_finder.some_word('wall'):
#         count += 1
#         if count == 10:
#             break
#         print ' '.join(str(member) for member in row_object)

