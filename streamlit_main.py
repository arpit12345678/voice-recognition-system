import streamlit as st
from command_executor import execute_command

st.set_page_config(page_title="Voice Assistant", layout="centered")
st.title("Voice Assistant: Web Email Sender")

st.markdown("Try commands like: `open google`, `search online cats`, or `send email`")

command = st.text_input("Enter your command:")

if "send email" in command.lower():
    with st.form("email_form"):
        to = st.text_input("Recipient Email")
        body = st.text_area("Message")
        submit = st.form_submit_button("Send Email")
        if submit:
            if to and body:
                execute_command("send email", to=to, body=body)
                st.success("Email sent successfully!")
            else:
                st.error("Both recipient and message are required.")
else:
    if st.button("Execute Command"):
        execute_command(command)
