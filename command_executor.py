import streamlit as st
from email_utils import send_email

def execute_command(command, to=None, body=None):
    command = command.lower()

    if "open google" in command:
        st.markdown("[Click here to open Google](https://www.google.com)", unsafe_allow_html=True)

    elif "send email" in command and to and body:
        send_email(to, body)
        st.success("Email sent successfully!")

    elif "search online" in command:
        query = command.replace("search online", "").strip()
        if query:
            url = f"https://www.google.com/search?q={query}"
            st.markdown(f"[Search results for '{query}']({url})", unsafe_allow_html=True)
        else:
            st.warning("Please provide a search term.")

    elif "exit" in command:
        st.info("You may close the app now.")

    else:
        st.warning("Command not recognized.")
