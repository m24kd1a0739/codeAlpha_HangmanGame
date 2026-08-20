# CodeAlpha Task 4: Basic Chatbot

print("======================================")
print("             BASIC CHATBOT")
print("======================================")

print("Chatbot: Hello! I am PyBot.")
print("Chatbot: Type 'bye' to exit.")

while True:
    user_input = input("\nYou: ").lower().strip()

    if user_input == "hello" or user_input == "hi":
        print("Chatbot: Hi! Nice to meet you.")

    elif user_input == "how are you":
        print("Chatbot: I'm fine, thank you!")

    elif user_input == "what is your name":
        print("Chatbot: My name is PyBot.")

    elif user_input == "what can you do":
        print("Chatbot: I can respond to simple predefined messages.")

    elif user_input == "thank you" or user_input == "thanks":
        print("Chatbot: You're welcome!")

    elif user_input == "bye":
        print("Chatbot: Goodbye! Have a great day!")
        break

    else:
        print("Chatbot: Sorry, I don't understand that.")

print("======================================")
print("Chatbot session ended.")
