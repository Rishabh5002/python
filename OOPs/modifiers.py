#public modifiers
class ABC:
    def __init__(self):
        self.public_attribute = None #this is public attribute 

    def public_function(): #this is public function 
        pass
     
#pprivate modifiers
class ABC:    
    def __init__(self):
        self.__private_attribute = None #this is private attribute
        
    def private_function(): #this is private function 
        pass
        
#protected modifiers 
class ABC:    
    def __init__(self):
        self._protected_attribute = None #this is protected attribute
        
    def _protected_function(): #this is protected function 
        pass
