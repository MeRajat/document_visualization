"""
    This class loads the document and parses it  
"""
from nltk import  ngrams
from nltk import StanfordPOSTagger


class Document(object):

    def __init__(self, path):
        self._path = path
        self._fp = open(self._path)
        self._st = StanfordPOSTagger('./stanford-jars/stanford-postagger-2016-10-31/models/english-bidirectional-distsim.tagger',
                                          path_to_jar = './stanford-jars/stanford-postagger-2016-10-31/stanford-postagger.jar')


    def read_line_tokenize(self):
        """
            This method read line by line and tokenize the line into 1-gram, 2-gram and 3-gram
        :return: list : 1-gram, 2-gram, 3-gram  
        """
        while True:
            data = self._fp.readline()
            if not data:
                break
            data = data.lower()
            gram_1 = ngrams(data.split(), 1)
            gram_2 = ngrams(data.split(), 2)
            gram_3 = ngrams(data.split(), 3)
            yield gram_1, gram_2, gram_3

    def pos_tagger(self, line):
        """
            this function performs the pos tagging  
        :return: words and it's tag 
        """











            yield data

