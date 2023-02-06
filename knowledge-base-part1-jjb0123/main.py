import unittest
import read, copy
from logical_classes import *
from student_code import KnowledgeBase

### Statement KB Tests ###
class KBTest(unittest.TestCase):

    def setUp(self):
        # Assert starter facts
        file = 'statements_kb.txt'
        data = read.read_tokenize(file)
        self.KB = KnowledgeBase([], [])
        for item in data:
            if isinstance(item, Fact):
                self.KB.kb_assert(item)
        

    def test1(self):
        ask1 = read.parse_input("fact: (color bigbox red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask([ask1])
        self.assertEqual(answer[0].bindings, [])

    def test2(self):
        ask1 = read.parse_input("fact: (color littlebox red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask([ask1])
        self.assertFalse(answer)

    def test3(self):
        ask1 = read.parse_input("fact: (color ?X red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask([ask1])
        self.assertIn("?X : bigbox", map(str, answer))
        self.assertIn("?X : pyramid3", map(str, answer))
        self.assertIn("?X : pyramid4", map(str, answer))
        

    def test4(self):
        ask1 = read.parse_input("fact: (color bigbox ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask([ask1])
        self.assertEqual(str(answer[0]), "?Y : red")

    def test5(self):
        ask1 = read.parse_input("fact: (color ?X ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask([ask1])
        self.assertIn("?X : bigbox, ?Y : red", map(str, answer))
        self.assertIn("?X : littlebox, ?Y : blue", map(str, answer))
        self.assertIn("?X : pyramid1, ?Y : blue", map(str, answer))
        self.assertIn("?X : pyramid2, ?Y : green", map(str, answer))
        self.assertIn("?X : pyramid3, ?Y : red", map(str, answer))
        self.assertIn("?X : pyramid4, ?Y : red", map(str, answer))

### Statement KB 2 Tests ###
class KBTest2(unittest.TestCase):

    def setUp(self):
        # Assert starter facts
        file = 'statements_kb2.txt'
        data = read.read_tokenize(file)
        self.KB = KnowledgeBase([], [])
        for item in data:
            if isinstance(item, Fact):
                self.KB.kb_assert(item)


    def test1(self):
        ask1 = read.parse_input("fact: (attacked Ai Nosliw)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask([ask1])
        self.assertEqual(answer[0].bindings, [])

    def test2(self):
        ask1 = read.parse_input("fact: (inst ?X ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask([ask1])
        self.assertIn("?X : Sarorah, ?Y : Sorceress", map(str, answer))
        self.assertIn("?X : Nosliw, ?Y : Dragon", map(str, answer))

    def test3(self):
        ask1 = read.parse_input("fact: (color bigbox blue)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask([ask1])
        self.assertFalse(answer)

    def test4(self):
        ask1 = read.parse_input("fact: (color bigbox ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask([ask1])
        self.assertFalse(answer)

### Statement KB 3 Tests ###
class KBTest3(unittest.TestCase):

    def setUp(self):
        # Assert starter facts
        file = 'statements_kb3.txt'
        data = read.read_tokenize(file)
        self.KB = KnowledgeBase([], [])
        for item in data:
            if isinstance(item, Fact):
                self.KB.kb_assert(item)


    def test1(self):
        ask1 = read.parse_input("fact: (inst Hershey dog)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask([ask1])
        self.assertEqual(answer[0].bindings, [])

    def test2(self):
        fact1 = read.parse_input("fact: (inst Hershey hero)")
        ask1 = read.parse_input("fact: (inst ?x hero)")
        ask2 = read.parse_input("fact: (friendly ?x)")
        self.KB.kb_assert(fact1)
        print(' Asking if', ask1, '\nAND', ask2)
        answer = self.KB.kb_ask([ask1, ask2])
        self.assertIn("?X : Ai", map(str, answer))
        self.assertIn("?X : Hershey", map(str, answer))

    def test3(self):
        ask1 = read.parse_input("fact: (inst ?x hero)")
        ask2 = read.parse_input("fact: (friendly ?x)")
        ask3 = read.parse_input("fact: (possesses ?x sword)")
        print(' Asking if', ask1, '\nAND', ask2, '\nAND', ask3)
        answer = self.KB.kb_ask([ask1, ask2, ask3])
        self.assertEqual(str(answer[0]), "?X : Ai")

    def test4(self):
        ask1 = read.parse_input("fact: (inst ?x hero)")
        ask2 = read.parse_input("fact: (friendly ?x)")
        ask3 = read.parse_input("fact: (inst ?x dog)")
        print(' Asking if', ask1, '\nAND', ask2, '\nAND', ask3)
        answer = self.KB.kb_ask([ask1, ask2, ask3])
        self.assertFalse(answer)

    def test5(self):
        ask1 = read.parse_input("fact: (inst ?x hero)")
        ask2 = read.parse_input("fact: (friendly ?x)")
        ask3 = read.parse_input("fact: (inst ?y dog)")
        ask4 = read.parse_input("fact: (travels-with-from-to ?x ?y town lake)")
        print(' Asking if', ask1, '\nAND', ask2, '\nAND', ask3, '\nAND', ask4)
        answer = self.KB.kb_ask([ask1, ask2, ask3, ask4])
        self.assertEqual(str(answer[0]), "?X : Ai, ?Y : Hershey")

if __name__ == '__main__':
    unittest.main()
