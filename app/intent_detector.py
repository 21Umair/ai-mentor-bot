import re

class IntentDetector:
    def __init__(self, intents):
        self.intents = intents
    
    def clean_text(self, text):
        "Convert text to lowercase and remove extra spaces."
        return text.lower().strip()
    
    def detect_intent(self, user_message):
        "This will detect the intent by matching user message with predefined patterns."
        user_message = self.clean_text(user_message)

        best_intent = "unknown"
        best_score = 0

        for intent_name, intent_data in self.intents.items():
            patterns = intent_data.get("patterns", [])

            for pattern in patterns:
                pattern = self.clean_text(pattern)

                if self.is_match(pattern, user_message):
                    score = len(pattern)

                    if score > best_score:
                        best_score = score
                        best_intent = intent_name
            
        return best_intent
    
    def is_match(self, pattern, user_message):
        "Check whether a pattern appears in the users message"
        escaped_pattern = re.escape(pattern)
        return re.search(r"\b" + escaped_pattern + r"\b", user_message) is not None