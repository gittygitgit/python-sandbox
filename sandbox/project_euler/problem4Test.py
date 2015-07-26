import problem4
import unittest

class TestFoo(unittest.TestCase):
  def test_isPalindrome(self):
    result=problem4.isPalindrome(123)
    self.assertFalse(result)	

    result=problem4.isPalindrome(111)
    self.assertTrue(result)	

    result=problem4.isPalindrome(9009)
    self.assertTrue(result)	

    result=problem4.isPalindrome(9008)
    self.assertFalse(result)	
	
if __name__ == '__main__':
    unittest.main()