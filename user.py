class USer:
    """
    Class that generates new instances of contacts
    """
    user_list=[]
    
    def __init__(self,first_name,last_name,username,password):
        
        self.first_name= first_name
        self.last_name= last_name
        self.username= username
        self.password= password