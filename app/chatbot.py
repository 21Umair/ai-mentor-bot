import json

from app.intent_detector import IntentDetector
from app.response_manager import ResponseManager
from app.state_manager import StateManager
from app.logger import setup_logger

class Chatbot:
    def __init__(self):
        self.intents = self.load_json("data\intents.json")
        self.learning_path = self.load_json("data\learning_paths.json")

        self.intent_detector = IntentDetector(self.intents)
        self.response_manager = ResponseManager(self.intents, self.learning_path)
        self.state_manager = StateManager()
        self.logger = setup_logger()

    def load_json(self, file_path):
        "Load JSON data from a file"
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
            
    def get_reply(self, user_message):
        "Recieve user message and return chatbot response."
        intent = self.intent_detector.detect_intent(user_message)

        self.state_manager.update_state(intent)
        user_state = self.state_manager.get_state()

        bot_response = self.response_manager.get_response(intent, user_state)

        self.logger.info(f"USER: {user_message}")
        self.logger.info(f"INTENT: {intent}")
        self.logger.info(f"STATE: {user_state}")
        self.logger.info(f"BOT: {bot_response}")

        return bot_response