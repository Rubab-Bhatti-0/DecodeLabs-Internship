
def main():
    """Main chatbot function implementing the IPO model."""
    responses = {
        'hello': 'Hi there! Welcome to the Rule-Based Chatbot. How can I help you today?',
        'hi': 'Hello! Nice to meet you. What can I do for you?',
        'hey': 'Hey! What\'s on your mind?',
        'how are you': 'I\'m functioning perfectly! Thanks for asking. How are you?',
        'what is your name': 'I\'m a Rule-Based Chatbot, built to demonstrate deterministic AI logic.',
        'who are you': 'I\'m your AI assistant powered by explicit if-else instructions and a knowledge base.',
        'help': 'I can respond to greetings, answer questions about myself, and discuss AI. Try asking me something!',
        'what can you do': 'I can greet you, tell you about myself, and have basic conversations using rule-based logic.',
        'bye': 'Goodbye! Thanks for chatting with me. See you next time!',
        'goodbye': 'Take care! It was nice talking to you.',
        'thanks': 'You\'re welcome! Happy to help.',
        'thank you': 'My pleasure! Feel free to ask me anything.',
        'what is ai': 'AI (Artificial Intelligence) is the simulation of human intelligence by machines. I\'m a deterministic rule-based system.',
        'explain logic engine': 'A logic engine processes inputs through explicit rules and decision trees to produce outputs. No hallucinations, 100% traceable.',
        'what is a chatbot': 'A chatbot is a conversational agent that responds to user inputs. I\'m a rule-based chatbot using dictionary lookups.',
    }
    
    # Welcome message
    print("=" * 70)
    print("RULE-BASED AI CHATBOT - Project 1")
    print("DecodeLabs Industrial Training Kit")
    print("=" * 70)
    print("\nWelcome! I'm a rule-based chatbot powered by deterministic logic.")
    print("Type 'help' to see what I can do, or 'exit'/'bye' to quit.\n")
    
    # Phase 1: INPUT LOOP
    while True:
        try:
            raw_input = input("You: ").strip()
            
            clean_input = raw_input.lower().strip()
            
            if clean_input in ['exit', 'quit', 'bye', 'goodbye']:

                exit_response = responses.get(clean_input, 'Goodbye!')
                print(f"Chatbot: {exit_response}")
                print("\nThank you for using the Rule-Based Chatbot!")
                break
            
            # Phase 2: PROCESS 
            response = responses.get(
                clean_input,
                "I don't understand that. Could you rephrase? Try 'help' for more info."
            )
            
            # Phase 3: OUTPUT 
            print(f"Chatbot: {response}\n")
            
        except KeyboardInterrupt:
            
            print("\n\nChatbot: Interrupted. Goodbye!")
            break
        except Exception as e:
            
            print(f"Chatbot: An error occurred: {e}. Please try again.\n")

if __name__ == "__main__":
    main()
