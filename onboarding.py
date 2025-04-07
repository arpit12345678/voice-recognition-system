import pyttsx3

def onboarding():
    engine = pyttsx3.init()
    message = """
    Welcome to your personal voice assistant.
    You can say things like:
    - Open Google
    - Open Notepad
    - Send Email
    - Exit
    """
    print(message)
    engine.say(message)
    engine.runAndWait()
