from app.chatbot import Chatbot

def main():
    bot = Chatbot()

    print("=" * 70)
    print("AI Career Mentor Bot")
    print("Personalized AI/ML guidance for begineer, intermediate, and advanced leaners.")
    print("Type 'exit' or 'quit' to stop the chatbot.")
    print("=" * 70)

    print("\nBot: Hello! I am your AI Career Montor Bot.")
    print("Bot: I can guide you based on your current AI/ML level.")
    print("Bot: Are you beginner, intermediate, or advanced?")

    while True:
        user_message = input("\nYou: ")
        if user_message.lower().strip() in ['exit', 'stop']:
            print("\nBot: Goodbye! Keep building projects and improving your portfolio.")
            break

    
        reply = bot.get_reply(user_message)
        print(f"\nBot: {reply}")

if __name__ == "__main__":
    main()