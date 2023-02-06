import read, copy
from util import *
from logical_classes import *

verbose = 0

class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules
        self.ie = InferenceEngine()

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def _get_fact(self, fact):
        """INTERNAL USE ONLY
        Get the fact in the KB that is the same as the fact argument

        Args:
            fact (Fact): Fact we're searching for

        Returns:
            Fact: matching fact
        """
        for kbfact in self.facts:
            if fact == kbfact:
                return kbfact

    def _get_rule(self, rule):
        """INTERNAL USE ONLY
        Get the rule in the KB that is the same as the rule argument

        Args:
            rule (Rule): Rule we're searching for

        Returns:
            Rule: matching rule
        """
        for kbrule in self.rules:
            if rule == kbrule:
                return kbrule

    def kb_add(self, fact_rule):
        """Add a fact or rule to the KB
        Args:
            fact_rule (Fact or Rule) - Fact or Rule to be added
        Returns:
            None
        """
        printv("Adding {!r}", 1, verbose, [fact_rule])
        if isinstance(fact_rule, Fact):
            if fact_rule not in self.facts:
                self.facts.append(fact_rule)
                for rule in self.rules:
                    self.ie.fc_infer(fact_rule, rule, self)
            else:
                if fact_rule.supported_by:
                    ind = self.facts.index(fact_rule)
                    for f in fact_rule.supported_by:
                        self.facts[ind].supported_by.append(f)
                else:
                    ind = self.facts.index(fact_rule)
                    self.facts[ind].asserted = True
        elif isinstance(fact_rule, Rule):
            if fact_rule not in self.rules:
                self.rules.append(fact_rule)
                for fact in self.facts:
                    self.ie.fc_infer(fact, fact_rule, self)
            else:
                if fact_rule.supported_by:
                    ind = self.rules.index(fact_rule)
                    for f in fact_rule.supported_by:
                        self.rules[ind].supported_by.append(f)
                else:
                    ind = self.rules.index(fact_rule)
                    self.rules[ind].asserted = True

    def kb_assert(self, fact_rule):
        """Assert a fact or rule into the KB

        Args:
            fact_rule (Fact or Rule): Fact or Rule we're asserting
        """
        printv("Asserting {!r}", 0, verbose, [fact_rule])
        self.kb_add(fact_rule)

    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Statement to be asked (will be converted into a Fact)

        Returns:
            listof Bindings|False - list of Bindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))
        if factq(fact):
            f = Fact(fact.statement)
            bindings_lst = ListOfBindings()
            # ask matched facts
            for fact in self.facts:
                binding = match(f.statement, fact.statement)
                if binding:
                    bindings_lst.add_bindings(binding, [fact])

            return bindings_lst if bindings_lst.list_of_bindings else []

        else:
            print("Invalid ask:", fact.statement)
            return []

    def kb_retract(self, fact_rule):
        """Retract a fact or a rule from the KB

        Args:
            fact_rule (Fact or Rule) - Fact or Rule to be retracted

        Returns:
            None
        """
        printv("Retracting {!r}", 0, verbose, [fact_rule])
        ####################################################
        if factq(fact_rule):
            kb_fr = self._get_fact(fact_rule)
        else:
            kb_fr = self._get_rule(fact_rule)

        if not kb_fr:
            return 
        if not kb_fr.supported_by:
            for f in kb_fr.supports_facts:
                for i in range(len(f.supported_by)):
                    new_supported_by = []
                    if kb_fr not in f.supported_by[i]:
                        new_supported_by.append(f.supported_by[i])
                f.supported_by = new_supported_by
                if not f.supported_by:
                    self.kb_retract(f)
            for k in kb_fr.supports_rules:
                for j in range(len(k.supported_by)):
                    new_support = []
                    if kb_fr not in k.supported_by[j]:
                        new_support.append(k.supported_by[j])
                k.supported_by = new_support 
                if not k.supported_by:
                    self.kb_retract(k)
                
            if factq(kb_fr):
                self.facts.remove(kb_fr)
            else:
                self.rules.remove(kb_fr)

    def kb_explain(self, answer):
        """Explain the support for a ListOfBindings

        Args:
            answer (ListOfBindigs) - list of bindings answer to be explained

        Returns: list of explanations for each binding in the answer

        """
        ####################################################
        # Student code goes here
        def kbe_hf(supported_fandr):
            dict = {}
            for i in supported_fandr:
                for j in i:
                    if factq(j):
                        dict["fact"] = {"name":str(j.statement),"asserted":j.asserted,"support": kbe_hf(j.supported_by)}
                    else: 
                        r_Str = "("
                        for k in j.lhs:
                            r_Str += str(k) + " "
                        r_Str = r_Str[:-1]
                        r_Str+= ")"
                        dict["rule"] = {"name":r_Str + " -> "+ str(j.rhs),"asserted":j.asserted,"support": kbe_hf(j.supported_by)}
            return [dict] if dict else None

        result = []
        for binding in answer.list_of_bindings:
            explanation = []
            for f in binding[1]:
                fact_dict = {"name":str(f.statement),"asserted":f.asserted,"support":kbe_hf(f.supported_by)}
                explanation.append(fact_dict)
            result.append(explanation)
        
        return result


class InferenceEngine(object):
    def fc_infer(self, fact, rule, kb):
        """Forward-chaining to infer new facts and rules

        Args:
            fact (Fact) - A fact from the KnowledgeBase
            rule (Rule) - A rule from the KnowledgeBase
            kb (KnowledgeBase) - A KnowledgeBase

        Returns:
            Nothing
        """
        printv('Attempting to infer from {!r} and {!r} => {!r}', 1, verbose,
            [fact.statement, rule.lhs, rule.rhs])
        ####################################################
        # Student code goes here
        a_binding = match(fact.statement, rule.lhs[0])
        if not a_binding:
            return 
        new_LHS = []
        new_Rule = instantiate(rule.rhs, a_binding)

        if len(rule.lhs) != 1:
            for i in range(1, len(rule.lhs)):
                new_LHS.append(instantiate(rule.lhs[i], a_binding))
            add_rule = Rule([new_LHS, new_Rule], [[fact, rule]])
            fact.supports_rules.append(add_rule)
            rule.supports_rules.append(add_rule)
            kb.kb_add(add_rule)
        else: 
            new_Fact = Fact(new_Rule, [[fact, rule]])
            fact.supports_facts.append(new_Fact)
            rule.supports_facts.append(new_Fact)
            kb.kb_add(new_Fact)

