def chatbot():
    print("🤖 Hello! I'm ChatBot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello"]:
            print("Bot: Hi there!")
        elif user_input in ["how are you", "how r u"]:
            print("Bot: I'm just code, but I'm doing great! 😊")
        elif user_input == "bye":
            print("Bot: Goodbye! 👋")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()