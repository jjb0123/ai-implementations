import math
import re

class Bayes_Classifier:

    def __init__(self):
    
        self.doc = 0


        self.numPosDict = None
        self.numNegDict = None

        self.sum_Pos_Dict = 0
        self.sum_Neg_Dict = 0

        self.pos_dict = {}
        self.neg_dict = {}

        self.num_pos_doc = 0
        self.num_neg_doc = 0

    def train(self, lines):
        data = self.helper(lines)
        self.pos_dict, self.neg_dict, self.num_pos_doc, self.num_neg_doc = self.words_func(data)
        #reinit self.doc to length of input
        self.doc = len(lines)
        #init positive dictionaries
        self.numPosDict = len(self.pos_dict)
        self.numNegDict = len(self.neg_dict)

        self.sum_Pos_Dict = sum(self.pos_dict.values())
        self.sum_Neg_Dict = sum(self.neg_dict.values())

        print(self.pos_dict)

    def classify(self, lines):
        reg = []
        data = self.helper(lines)
        
        for i in data:
            #calculate probs

            negative_probability = math.log(self.num_neg_doc / self.doc)
            positive_probability = math.log(self.num_pos_doc / self.doc)
            #iterative probabilities
            for word in i[2:]:
                if word in self.neg_dict.keys():
                    negative_probability = negative_probability + math.log((self.neg_dict[word] + 1) / (self.numNegDict + self.sum_Neg_Dict))
                else:
                    negative_probability = negative_probability + math.log(1 / (self.numNegDict + self.sum_Neg_Dict+ self.sum_Pos_Dict))

                if word in self.pos_dict.keys():
                    positive_probability = positive_probability + math.log((self.pos_dict[word] + 1) / (self.numPosDict+self.sum_Pos_Dict))
                else:
                    positive_probability = positive_probability + math.log(1 / (self.numPosDict + self.sum_Pos_Dict+ self.sum_Neg_Dict))

            #review comparisons   
            if positive_probability < negative_probability:
                reg.append('1')
                
            else:
                reg.append('5')

        return reg

    def words_func(self,data):

        num_neg_doc = 0
        num_pos_doc = 0

        positive_dictionary = {}
        negative_dictionary = {}
      
       
        for i in data:
            #if five star review
            if i[0] == '5':
                num_pos_doc = num_pos_doc + 1
                for word in i[2:]:
                    if word not in positive_dictionary.keys():
                        positive_dictionary[word] =  1
                        
                    else:
                        positive_dictionary[word] = positive_dictionary[word] +1
            #if one star review
            if i[0] == '1':
                num_neg_doc = num_neg_doc + 1
                for word in i[2:]:
                    if word in negative_dictionary.keys():
                        negative_dictionary[word] = negative_dictionary[word] + 1
                    else:
                        negative_dictionary[word] = 1
        #return all elems   
        return positive_dictionary,negative_dictionary,num_pos_doc,num_neg_doc

    def helper(self,lines):
        array = []
        for i in lines:
            array.append(i.split('|'))
        for i in array:
            i[2] = self.remove_stop(i[2])
            i[2:] = i[2].split(' ')
        return array

   
    def remove_stop(self,txt):
        txt = txt.lower()
        txt = txt.replace(".", " ")
        txt = txt.replace(",", " ")
        txt = txt.replace(":", " ")
        txt = txt.replace("(", " ")
        txt = txt.replace("<", " ")
        txt = txt.replace(">", " ")
        txt = txt.replace(";", " ")
        txt = txt.replace("?", " ")
        txt = txt.replace("there ", " ")
        txt = txt.replace("with ", " ")
        txt = txt.replace("is ", " ")
        txt = txt.replace("are ", " ")
        txt = txt.replace("$", " ")
        txt = txt.replace("%", " ")
        txt = txt.replace(")", " ")
        txt = txt.replace("for ", " ")
        txt = txt.replace("i ", " ")
        txt = txt.replace("and ", " ")
        txt = txt.replace("-", " ")
        txt = txt.replace("this ", " ")
        txt = txt.replace("its ", " ")
        txt = txt.replace("me ", " ")
        txt = txt.replace("make ", " ")
        txt = txt.replace("him ", " ")
        txt = txt.replace("she ", " ")      
        txt = txt.replace("/", " ")
        txt = txt.replace("#", " ")
        txt = txt.replace("'", " ")
        txt = txt.replace("in ", " ")
        txt = txt.replace("as ", " ")
        txt = txt.replace("@", " ")
        txt = txt.replace("that ", " ")
        txt = txt.replace("his ", " ")
        txt = txt.replace("these ", " ")
        txt = txt.replace("\n", ' ')
        txt = txt.replace(r"\\", ' ')
        txt = txt.replace("!", " ")
        txt = txt.replace("*", " ")
        txt = txt.replace("a ", " ")
        txt = txt.replace("it's ", " ")        
        txt = txt.replace("it ", " ")
        txt = txt.replace("he ", " ")
        txt = txt.replace(r'\r', ' ')
        txt = txt.replace("an ", " ")
        txt = txt.replace("to ", " ")
        txt = txt.replace("on ", " ")
        txt = txt.replace(r'\r', ' ')
        txt = txt.replace("the ", " ")
        txt = txt.replace("of ", " ")
    
       
      


        chars = "!#$%&()*+,-./:;<=>?@[\]^_`{'~}"
        chars += '"1234567890'
        for i in chars:
            txt = txt.replace(i, ' ')

        return txt