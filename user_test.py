import unittest
from user import User
class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
    unittest.TestCase: TestCase class that helps in creatingtest cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_User= User("Anais","simp","Anasimp","213123")

    def test_init (self):
         '''
         test_init test case to test if the object is initialized properly
         '''
         self.assertEqual(self.new_User.first_name,"Anais")
         self.assertEqual(self.new_User.last_name,"simp")
         self.assertEqual(self.new_User.username,"Anasimp")
         self.assertEqual(self.new_User.password,"213123")
if __name__ == '__main__':
    unittest.main()