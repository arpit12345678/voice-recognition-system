import webbrowser
from email_utils import send_email

def execute_command(command):
    if "open google" in command:
        webbrowser.open("https://www.google.com")
    elif "send email" in command:
        to = input("Enter recipient email: ")
        body = input("Enter message: ")
        send_email(to, body)
    elif "search online" in command:
        query = command.replace("search for", "")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        print(f"Searching for {query}")
    elif "exit" in command:
        print("Exiting. Goodbye!")
        exit()
    else:
        print("Command not recognized.")
