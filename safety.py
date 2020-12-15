

class Safety:

    def __init__(self):
        self.__key = -3
    

    def encryp_message(self, text: str):

        msg = ''
        for char in text:
            msg += chr(ord(char) + self.__key)
        
        return msg
        
    
    def decrypt_message(self, text: str):

        msg = ''
        for char in text:
            msg += chr(ord(char) - self.__key)
        return msg