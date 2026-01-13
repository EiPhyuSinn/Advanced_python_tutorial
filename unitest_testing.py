import unittest

def add(a, b):
    return a + b

def divide(a:int,b:int)-> float:
    try: 
        result = a/b 
    except ZeroDivisionError:
        print("Cannot divide with zero")
        raise ZeroDivisionError
    else:
        return result


class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5) 
    
    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10,0)
        self.assertEqual(divide(10,2),5.0)

if __name__ == '__main__':
    unittest.main()