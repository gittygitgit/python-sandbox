import problem5
import unittest

class TestFoo(unittest.TestCase):
  def test_isEvenlyDivisible(self):
    result=problem5.isEvenlyDivisible(100)
    self.assertFalse(result)		
	
if __name__ == '__main__':
    unittest.main()
