import random

class ResponseManager:
    def __init__(self, intents, learning_paths):
        self.intents = intents
        self.learning_paths = learning_paths

    def get_response(self, intent, user_state):
        "Generate a response based on intent and user state"
        if intent =="beginner_level":
            user_state["level"] = "beginner"
            return self.get_learning_path("beginner")
        
        if intent == "basic_knowledge":
            user_state["level"] = "beginner"
            return (
                "Got it. You seem to have some basic knowledge, but not enough detail yet.\n\n"
                "I will place you at an advanced-beginner level for now.\n\n"
                "Recommended next steps:\n"
                "1. Revise Python basics\n"
                "2. Learn NumPy and Pandas\n"
                "3. Learn basic statistics\n"
                "4. Start machine learning fundamentals\n"
                "5. Build 2 small beginner projects\n\n"
                "After that, you can move to intermediate projects."
            )
        
        if intent =="intermediate_level":
            user_state["level"] = "intermediate"
            return self.get_learning_path("intermediate")
        
        if intent =="advanced_level":
            user_state["level"] = "advanced"
            return self.get_learning_path("advanced")
        
        if intent == "portfolio_projects":
            return self.get_project_recommendations(user_state)
        
        responses = self.intents.get(intent, self.intents["unknown"]).get("response", [])

        if not responses:
            return "I do not have a response for that yet."
        
        return random.choice(responses)
    
    def get_learning_path(self, level):
        "Return a formatted roadmap based on user's level"

        path = self.learning_paths.get(level)

        if not path:
            return "I could not find a learning path for this level."
        
        response = f"{path['titile']}\n\n"
        response += f"{path['description']}\n\n"
        response += "Recommended Steps:\n"

        for index, step in enumerate(path["steps"], start=1):
            response += f"{index}. {step}\n"

        for index, project in enumerate(path["recommended_projects"], start=1):
            response += f"{index}. {project}\n"

            return response
        
    def get_project_reommendations(self, user_state):
        "Recommend projects based on the user's saved level"
        level = user_state.get("level")

        if level is None:
            return("I can suggest better project if I know your current level. "
                   "Are you a beginner, intermediate, or advanced?"
                   )
        
        path = self.learning_paths.get(level)

        if not path:
            return "I could not find project recommendations for your level."
        
        response = f"Based on you {level} level, here are suitable portfolio projects:\n\n"

        for index, project in enumerate(path["recommend_projects"], start=1):
            response += f"{index}. {project}\n"

        return response