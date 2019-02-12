import unittest
from user import User
class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_User= User("Anais","simp","Anasimp","213123")

    def test_init (self):
        '''
        test_init test case to test if the object is initialized properly.
        '''
        self.assertEqual(self.new_User.first_name,"Anais")
        self.assertEqual(self.new_User.last_name,"simp")
        self.assertEqual(self.new_User.username,"Anasimp")
        self.assertEqual(self.new_User.password,"213123")
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_User.save_user()
        self.assertEqual(len(User.user_list),1)
        # Items up here...

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_User.save_user()
            test_user = User("Anais","simp","Anasimp","213123") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
    def test_user_exists(self):
            '''
            test to check if we can return a Boolean  if we cannot find the contact.
            '''
            self.new_User.save_user()
            test_user = User("Anais","simp","Anasimp","213123") # new user
            test_user.save_user()
            user_exists = User.user_exist("Anasimp")
            self.assertTrue(user_exists)
if __name__ == '__main__':
    unittest.main()