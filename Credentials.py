class Credentials: 
    """
    Class that generates new instances of Credentials
    """
    Credentials_list = [] #Empty Credentials list
    def __init__(self, website_name,user_name,password):
        
        # docstring removed for simplicity

        self.website_name = website_name
        self.user_name = user_name
        self.password = password

    Credentials_list = [] # Empty Credentials list
    # Init method up here
    def save_Credentials(self):

        '''
        save_credential method saves credential objects into credential_list
        '''

        Credentials.Credentials_list.append(self)

    def delete_Credentials(self):

        '''
        delete Credentials method deletes a saved Credentials from the Credentials_list
        '''
        Credentials.Credentials_list.remove(self)
    @classmethod
    def find_by_name(cls,name):
        '''
        Method that takes in a name and returns a Credentials that matches that name.
        Args:
            name: Phone name to search for
        Returns :
            Credentials of person that matches the name.
        '''

        for Credentials in cls.Credentials_list:
            if Credentials.website_name == name:
                return Credentials
    @classmethod
    def Credentials_exist(cls,website_name):
        '''
        Method that checks if a user exists from the Credential list.
        Args:
            website_name:website_name to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for Credentials in cls.Credentials_list:
            if Credentials.website_name == website_name:
                return True

       
    @classmethod
    def display_Credentials(cls):
        '''
        method that returns the Credentials list
        '''
        return cls.Credentials_list