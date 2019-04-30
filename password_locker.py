import uuid #module for generating random strings
import pyperclip
class Password_Locker:

    """
    class that generates new instance of password locker
    """

    def __init__(self,username,password):

        '''
        __init__ method that helps us define properties for our objects

        Args:
            username : New or existing passwordlocker account
            password : New or existing passwordlocker account
        '''
        self.username = username
        self.password = password
        self.filename = self.username+".txt"
        self.credential_filename = "credentials_"+ self.filename

    def create_account(self):
        '''
        Function that reads username and password and creates a new account

        Raises:
                FileExistsError if the account exists
        '''
        try:
             with open(self.filename,"w+") as handle:
                handle.write(self.password)
                return True

        except FileExistsError:
                            return False

    def login(self):
        '''
        Function that reads username and password and logs in
        Return :
                True - Login Succesful
                False - Account Does not Exist
        Raises  :
                FileNotFoundError: If it cannot find the user
        
        '''

        try :
            with open(self.filename,"r") as handle:
                data = handle.readline()
                if data == self.password:
                    return True
                else:
                    return False

        except FileNotFoundError:
            return False
            
        
    def add_credentials(self,acc,acc_username,acc_password):

            '''
            Function that adds user's credentials

            Raises:
                    FileNotFoundError : If user has no account
            '''
            data = "\n" + acc + ": " +"username " + acc_username + " " + " password "+ acc_password
            try:
                handle =  open(self.credential_filename,"a") 
                handle.write(data)
                handle.close()
                return True
            except FileNotFoundError:
                    return False

    def generate_credentials(self):

        '''
        Function that generates users credentials

        Returns :
                account_name : username password
        '''
        
        with open(self.credential_filename,"r") as handle:
            data = handle.read()

            return data

    def generate_password(self,length=8):
        '''
        Function that generates passwords

        Returns :
                random passwords
        '''

        randomString = uuid.uuid4().hex #get a random string in a UUID format
        randomString = randomString[0:length]

        return randomString

    def copy_credentials(self):
        '''
        Function that copies credentials on clipboard using pyperclip module
        '''
        with open(self.credential_filename,"r") as handle:
            data = handle.read()
            pyperclip.copy(data)
        
    def set_password_length(self,length):
        '''
        Function that returns a password of a given length
        '''
        return Password_Locker.generate_password(self,length)