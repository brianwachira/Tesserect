class Password_locker:

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

