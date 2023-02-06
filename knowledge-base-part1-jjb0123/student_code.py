from distutils.log import error
from pickle import FALSE, TRUE
from queue import Empty
import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):

        print("Asserting {!r}".format(fact))
        if fact not in self.facts:
            self.facts.append(fact)

               
        """Assert a fact or rule into the KB
        
        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
      
        
    def kb_ask(self, facts):

        print("Asking {!r}".format(facts))

        list_results = ListOfBindings()

        for fact in facts:    
            x = 0
            if not factq(fact):
                return False
            for f in self.facts: 
                matched_facts = match(fact.statement, f.statement, bindings=None)
                if matched_facts:
                    x = 1
                    list_results.add_bindings(matched_facts, self.facts)
            if x < 1:
                return False
        if not list_results:
            return False
        else:
            return list_results
        # Args:
        #     fact (Fact) - Fact to be asked

        # Returns:
        #     ListOfBindings|False - ListOfBindings if result found, False otherwise
        # """
        
