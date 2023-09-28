import unittest
def check(x):
	return x == 'PEDRO'
class check(unittest.TestCase):
	def test(self):
		self.assertEqual(check(PEDRO),PEDRO)
if __name__=='__main__':
	unittest.main()
