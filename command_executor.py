import webbrowser
import os
from email_utils import send_email

def execute_command(command):
    if "open google" in command:
        webbrowser.open("https://www.google.com")
    elif "open notepad" in command:
        os.system("notepad.exe")
    elif "send email" in command:
        to = input("Enter recipient email: ")
        body = input("Enter message: ")
        send_email(to, body)
    elif "exit" in command:
        print("Exiting. Goodbye!")
        exit()
    else:
        print("Command not recognized.")
