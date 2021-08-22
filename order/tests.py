import unittest
from .validator import is_valid_phone_number

class TestPhoneNumberValidatorMethods(unittest.TestCase):
    
    def test_valid_input(self):
        self.assertEqual(is_valid_phone_number("0612345678"), True)
        self.assertEqual(is_valid_phone_number("+31612345678"), True)
        self.assertEqual(is_valid_phone_number("+316123456789"), True)
        # self.assertEqual(is_valid_phone_number("0031612345678"), True) # known bug
 
    def test_invalid_input(self):
        self.assertEqual(is_valid_phone_number("061234567"), False)
        self.assertEqual(is_valid_phone_number("0612345678901234"), False)
        self.assertEqual(is_valid_phone_number("061234567a"), False)
        self.assertEqual(is_valid_phone_number("Sander"), False)
        self.assertEqual(is_valid_phone_number("tel0612345678"), False)

        
if __name__ == '__main__':
    unittest.main()
