import webbrowser
from email_utils import send_email

def execute_command(command, to=None, body=None):
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://www.google.com")

    elif "send email" in command and to and body:
        send_email(to, body)

    elif "search online" in command:
        query = command.replace("search online", "").strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            print(f"Searching for {query}")
        else:
            print("Please provide a search query.")

    elif "exit" in command:
        print("Exiting. Goodbye!")
        exit()

    else:
        print("Command not recognized.")
