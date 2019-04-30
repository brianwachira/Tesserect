import unittest #Importing the unittest module
from password_locker import Password_Locker #Importing password class
import uuid #module for generating random strings
import pyperclip
class TestPassword(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_password_locker = Password_Locker("password_locker_test","passwordlocker123")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_password_locker.username,"password_locker_test")
        self.assertEqual(self.new_password_locker.password,"passwordlocker123")

    def test_create_account(self):
        '''
        test to confirm account is created
        '''
        self.assertTrue(Password_Locker.create_account(self.new_password_locker))

    def test_login(self):
        '''
        test to confirm login
        '''
        self.assertTrue(Password_Locker.login(self.new_password_locker))

    def test_add_credentials(self):
        '''
        test to confirm credentials are added
        '''
        self.assertTrue(Password_Locker.add_credentials(self.new_password_locker,"facebook","wildcard","134dea"))    

    def test_generate_credentials(self):
        '''
        test to display credentials
        '''
        Password_Locker.add_credentials(self.new_password_locker,"facebook","wildcard","134dea")

        with open(self.new_password_locker.credential_filename,"r") as handle:
            data = handle.read()
        self.assertEqual(Password_Locker.generate_credentials(self.new_password_locker),data)

    def test_generate_password(self,length = 8):
        '''
        test to generate passwords
        '''
        test_string = uuid.uuid4().hex
        test_string = test_string[0:length]
        self.assertNotEqual(Password_Locker.generate_password(self.new_password_locker),test_string)

    def test_copy_credentials(self):
        '''
        test to copy credentials on clipboard
        '''

        self.assertEqual(Password_Locker.generate_credentials(self.new_password_locker),pyperclip.paste())



if __name__ == "__main__":
     unittest.main()   