from app.model.login import LoginDTO
from random import randint


class Session:
    
    def __init__(self) -> None:
        self.session_container = {}

    def create_session(self, token: str, user_id: int):
        self.session_container['token'] = token
        self.session_container['user_id'] = user_id
        
    def clear_session(self):
        self.session_container.clear()
        
    def get_user_data(token):
        print("TODO")
        # validate if session is OK, return userIdentifier.
        
session = Session()