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
        self.filename = username+".txt"

    def create_account(self):
        
        try:
            with open(self.username+".txt","r")as handle:
                return False

        except FileNotFoundError:
             with open(self.username+".txt","w") as handle:
                handle.write(self.password)
                return True

    def add_credentials(self,acc,acc_username,acc_password):

            try:
                with open(self.filename,"a") as handle:
                    data = acc + ": " +"username " + acc_username + " " + " password "+ acc_password
                    handle.write(data)
                    return True
            except:
                    return False
                    