# chat.py
# MMORPG chat system

class Chat:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, message):
        self.messages.append({'sender': sender, 'message': message})

    def get_messages(self, last_n=10):
        return self.messages[-last_n:]
