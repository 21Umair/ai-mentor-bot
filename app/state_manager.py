class StateManager:
    def __init__(self):
        self.user_state = {
            "level": None,
            "last_intent": None,
            "message_count": 0
        }
    
    def update_state(self, intent):
        "Update conversation state after every user message"
        self.user_state["last_intent"] = intent
        self.user_state["message_count"] += 1

    def set_level(self, level):
        "Save the user's detected level."
        self.user_state["level"] = level

    def get_state(self):
        "Return current user state"
        return self.user_state