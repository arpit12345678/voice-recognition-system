from onboarding import onboarding
from recognizer import recognize_speech
from command_executor import execute_command

def main():
    print("Welcome to the Voice Recognition System!")
    onboarding()

    while True:
        print("\nListening... (say 'exit' to quit)")
        text = recognize_speech()

        if text:
            print(f"You said: {text}")
            if text.lower() == "exit":
                print("Exiting the system. Goodbye!")
                break
            execute_command(text)
        else:
            print("Sorry, I didn't catch that.")

if __name__ == "__main__":
    main()
