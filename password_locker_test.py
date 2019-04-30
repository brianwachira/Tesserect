import unittest #Importing the unittest module
from password_locker import Password_Locker #Importing password class
import uuid #module for generating random strings

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
        password_locker_test = Password_Locker("password_locker_test","passwordlocker123")

        self.assertTrue(Password_Locker.create_account(password_locker_test))

    def test_login(self):
        '''
        test to confirm login
        '''
        password_locker_test = Password_Locker("password_locker_test","passwordlocker123")

        self.assertTrue(Password_Locker.login(password_locker_test))

    def test_add_credentials(self):
        '''
        test to confirm credentials are added
        '''
        password_locker_test = Password_Locker("password_locker_test","passwordlocker123")

        self.assertTrue(Password_Locker.add_credentials(password_locker_test,"facebook","wildcard","134dea"))    

    def test_generate_credentials(self):
        '''
        test to display credentials
        '''
        password_locker_test = Password_Locker("password_locker_test","passwordlocker123")
        Password_Locker.add_credentials(password_locker_test,"facebook","wildcard","134dea")

        with open(password_locker_test.credential_filename,"r") as handle:
            data = handle.read()
        self.assertEqual(Password_Locker.generate_credentials(password_locker_test),data)

    def test_generate_password(self):
        '''
        test to generate passwords
        '''
        test_string = uuid.uuid4().hex
        test_string = test_string[0:8]
        self.assertNotEqual(Password_Locker.generate_password(self.new_password_locker),test_string)

if __name__ == "__main__":
     unittest.main()   