import unittest #IMporting the unittest module
from password_locker import Password_Locker #Importing password class

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

        self.assertEqual(Password_Locker.create_account(password_locker_test),True)

    def test_login(self):
        '''
        test to confirm login
        '''
        password_locker_test = Password_Locker("password_locker_test","passwordlocker123")

        self.assertEqual(Password_Locker.login(password_locker_test),True)

    def test_add_credentials(self):
        '''
        test to confirm credentials are added
        '''
        password_locker_test = Password_Locker("password_locker_test","passwordlocker123")

        self.assertEqual(Password_Locker.add_credentials(password_locker_test,"facebook","wildcard","134dea"),True)    

if __name__ == "__main__":
     unittest.main()   