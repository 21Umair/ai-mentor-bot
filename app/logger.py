import logging

def setup_logger():
    logging.basicConfig(
        filename = "logs/conversation.log",
        level = logging.INFO,
        format = "%(asctime)s - %(message)s"
    )

    return logging.getLogger("chatbot_logger")