class Credentials:
    """
     Class that generates new instances of credentials
    """
    credential_list=[]
    def __init__(self,website_name,username,password):
        
        self.website_name= website_name
        self.last_name= username
        self.username= password
        
    credentials_list= []