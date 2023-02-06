from bayesnet import BayesNet, BayesNode
import student_code as sc
import unittest

class BayesTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.bn = sc.makeCancerNet()

	def test1a(self):
		a = sc.ask('Age', True, {}, BayesTest.bn)
		print('P(a)', a)
		self.assertAlmostEqual(0.6, a)

	def test1b(self):
		c = sc.ask('Genes', True, {}, BayesTest.bn)
		print('P(g)=', c)
		self.assertAlmostEqual(0.2, c)

	def test2a(self):
		c = sc.ask('Cancer', True, {'Age':True, 'Genes':True}, BayesTest.bn)
		print('P(c|a,g)=', c)
		self.assertAlmostEqual(0.1, c)

	def test2b(self):
		c = sc.ask('Cancer', False, {'Age':True, 'Genes':True}, BayesTest.bn)
		print('P(¬c|a,g)=', c)
		self.assertAlmostEqual(0.9, c)

	def test2c(self):
		c = sc.ask('Cancer', False, {'Age':True, 'Genes':False}, BayesTest.bn)
		print('P(¬c|a,¬g)=', c)
		self.assertAlmostEqual(0.99, c)

	def test2d(self):
		c = sc.ask('Test', 'Positive', {'Cancer': True}, BayesTest.bn)
		print('P(t|c)=', c)
		self.assertAlmostEqual(0.9821428571428571, c, places=4)

	def test2e(self):
		c = sc.ask('Treatment', True, {'Test': 'Positive'}, BayesTest.bn)
		print('P(tr|te)=', c)
		self.assertAlmostEqual(0.9927884615384616, c, places=4)

	def test2f(self):
		c = sc.ask('Prognosis', 1, {'Treatment': True}, BayesTest.bn)
		print('P(p==1|tr)=', c)
		self.assertAlmostEqual(0.10139041597453123, c, places=4)

	def test3(self):
		g = sc.ask('Genes', True, {'Cancer':True}, BayesTest.bn)
		print('P(g|c)=', g)
		self.assertAlmostEqual(0.7142857142857143, g, places=4)

	def test4(self):
		p = sc.ask('Prognosis', 5, {'Age':True, 'Test':'Positive'}, BayesTest.bn)
		print('P(p==5|a,t)=', p)
		self.assertAlmostEqual(0.14891826923076923, p, places=4)

	def test5(self):
		c = sc.ask('Genes', True, {'Test':'Positive'}, BayesTest.bn)
		print('P(g|t)=', c)
		self.assertAlmostEqual(0.46642596356180643, c, places=4)


if __name__== "__main__":
	unittest.main()


