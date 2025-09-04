import unittest

def add(a, b):
  """
  This function takes two numbers as input and returns their sum.

  Args:
    a: The first number.
    b: The second number.

  Returns:
    The sum of a and b.
  """
  return a + b

def secure_add(a, b):
    """
    Adds two numbers securely.
    
    This function performs a simple addition and is secure
    because it only works on numerical data types. It does
    not use any user-provided strings in a way that could
    lead to code injection or other vulnerabilities.
    
    Args:
        a (int, float): The first number.
        b (int, float): The second number.
    
    Returns:
        int, float: The sum of a and b.
    """
    
    # Check if both inputs are numbers to prevent type-related issues.
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numbers (integers or floats).")
        
    return a + b

class TestExercise1(unittest.TestCase):
    
    def testAdd1(self):
        self.assertEqual(add(1, 2), 3)

    def testAdd2(self):
        self.assertEqual(add(1.125, 2.25), 3.375)

    def testAdd3(self):
        self.assertEqual(add(-1, 4), 3)

    def testAdd4(self):
        self.assertEqual(add(1, 3+4j), 4+4j)

    def testAdd5(self):
        self.assertEqual(add(1, float('inf')), float('inf'))

    def testSecureAdd1(self):
        self.assertEqual(secure_add(1, 2), 3)

    def testSecureAdd2(self):
        self.assertEqual(secure_add(1.125, 2.25), 3.375)

    def testSecureAdd3(self):
        self.assertEqual(secure_add(-1, 4), 3)

    def testSecureAdd4(self):
        try:
            secure_add(1, 3+4j), 4+4j
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)

    def testSecureAdd5(self):
        self.assertEqual(secure_add(1, float('inf')), float('inf'))

if __name__ == '__main__':
    unittest.main()