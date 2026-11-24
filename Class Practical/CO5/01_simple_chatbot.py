"""A small rule-based chatbot using simple text matching."""
def reply(message):
    text = message.lower().strip()
    if any(word in text for word in ["hello", "hi", "hey"]):
        return "Hello! How can I help you?"
    if "name" in text: return "I am a simple Python chatbot."
    if "help" in text: return "You can ask about my name, time, or say bye."
    if "time" in text:
        from datetime import datetime
        return "Current time: " + datetime.now().strftime("%H:%M:%S")
    if any(word in text for word in ["bye", "exit", "quit"]):
        return "Goodbye!"
    return "Sorry, I did not understand. Please try another question."

if __name__ == "__main__":
    while True:
        message = input("You: ")
        answer = reply(message)
        print("Bot:", answer)
        if answer == "Goodbye!": break
