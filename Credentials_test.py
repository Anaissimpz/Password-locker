import unittest
from Credentials import Credentials
class TestUnit(unittest.TestCase):
    '''
    Test class that defines test cases for the Credentials class behaviours.
    Args:
    unittest.TestCase:TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_Credentials=Credentials("Twitter","Anasimp","password")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_Credentials.website_name,"Twitter")
        self.assertEqual(self.new_Credentials.user_name,"Anasimp")
        self.assertEqual(self.new_Credentials.password,"password")
    

    def test_save_Credentials(self):
        '''
        test_save_Credentials test case to test if the Credentials object is saved into
        the Credentials list
        '''
        self.new_Credentials.save_Credentials() # saving the new Credentials
        self.assertEqual(len(Credentials.Credentials_list),1)

    # setup and class creation up here

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.Credentials_list = []

    # other test cases here
    def test_save_multiple_Credentials(self):
            '''
            test_save_multiple_Credentials to check if we can save multiple Credentials
            objects to our Credentials_list
            '''
            self.new_Credentials.save_Credentials()
            test_Credentials = Credentials("Twitter","Anasimp","password") # new credentials
            test_Credentials.save_Credentials()
            self.assertEqual(len(Credentials.Credentials_list),2)

    # More tests above
    def test_delete_Credentials(self):
            '''
            test_delete_Credentials to test if we can remove a credentials from our credentials list
            '''
            self.new_Credentials.save_Credentials()
            test_Credentials = Credentials("Twitter","Anasimp","password") # new Credentials
            test_Credentials.save_Credentials()

            self.new_Credentials.delete_Credentials()# Deleting a Credentials object
            self.assertEqual(len(Credentials.Credentials_list),1)

    def test_find_credentials_by_name(self):
        '''
        test to check if we can find a Credentials by phone name and display information
        '''

        self.new_Credentials.save_Credentials()
        # self.new_Credentials.save_Credentials()
        test_Credentials = Credentials("Twitter","Anasimp","password") # new Credentials
        test_Credentials.save_Credentials()

        found_Credentials = Credentials.find_by_name("Twitter")

        self.assertEqual(found_Credentials.user_name,test_Credentials.user_name)
    def test_Credentials_exists(self):
            '''
            test to check if we can return a Boolean  if we cannot find the Credentials.
            '''
            self.new_Credentials.save_Credentials()
            test_Credentials =Credentials("Twitter","Anasimp","password") # new user
            test_Credentials.save_Credentials()
            Credentials_exists = Credentials.Credentials_exist("Twitter")
            self.assertTrue(Credentials_exists)

    def test_display_all_Credentials(self):
        '''
        method that returns a list of all Credentials saved
        '''

        self.assertEqual(Credentials.display_Credentials(),Credentials.Credentials_list)


if __name__ ==  '__main__':
    unittest.main()