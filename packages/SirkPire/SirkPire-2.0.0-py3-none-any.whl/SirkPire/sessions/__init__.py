import os
from json import loads, dumps

class sessions:

    def __init__(self):
        pass

    def cheack_session(self, session_name):
        return os.path.exists(f'{session_name}.SirkPire')
    
    def session_data(self, session_name):
        return loads(open(f'{session_name}.SirkPire', encoding='UTF-8').read())
        
    def create_session(self, session_name, session_data):
        open(f'{session_name}.SirkPire', 'w', encoding='UTF-8').write(dumps(session_data, indent=4))