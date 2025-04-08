import streamlit as st
from command_executor import execute_command

st.set_page_config(page_title="Voice Recognition Assistant", layout="centered")

st.title("🎙️ Voice Recognition System (Web Mode)")
st.markdown("""
    Welcome to your personal voice assistant.
    Type a command below instead of speaking (voice not supported on cloud).
    - Open Google
    - Send Email
    - Search Online
    - Exit
""")

command = st.text_input("Enter your command:")

if st.button("Execute"):
    if command:
        st.write(f"You entered: `{command}`")
        execute_command(command.lower())
    else:
        st.warning("Please enter a command.")
