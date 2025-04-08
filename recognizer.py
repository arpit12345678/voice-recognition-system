def recognize_speech():
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
        return recognizer.recognize_google(audio).lower()
    except Exception as e:
        print(f"[Fallback Mode] Speech recognition not available: {e}")
        return input("Type your command instead: ").lower()
