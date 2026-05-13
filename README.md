# AI Career Mentor Bot

AI Career Mentor Bot is a rule-based chatbot that provides personalized AI/ML career guidance for beginner, intermediate, and advanced learners.

## Features

- Rule-based intent detection
- Personalized AI/ML roadmaps
- Beginner, intermediate, and advanced learning paths
- Portfolio project recommendations
- JSON-based chatbot knowledge base
- Conversation state management
- Conversation logging
- Modular Python code structure
- Ready for future FastAPI and Telegram integration

## Tech Stack

- Python
- Regex
- JSON
- Logging

## Project Structure

```text
ai-career-mentor-bot/
│
├── app/
│   ├── __init__.py
│   ├── intent_detector.py
│   ├── state_manager.py
│   ├── response_manager.py
│   ├── logger.py
│   └── chatbot.py
│
├── data/
│   ├── intents.json
│   └── learning_paths.json
│
├── logs/
│   └── conversations.log
│
├── main.py
├── requirements.txt
└── README.md