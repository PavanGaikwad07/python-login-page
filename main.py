import streamlit as st

# Dictionary containing email and password pairs
a = {
    "FS23AI001@gmail.com": "12345",
    "FS23AI002@gmail.com": "12345",
    "FS23AI003@gmail.com": "12345",
    "FS23AI004@gmail.com": "12345"
}

email = st.text_input('Enter email - ')
password = st.text_input('Enter Password - ', type='password')  # Password field
btn = st.button('Login')

if btn:
    if email in a and password == a[email]:  # Check if email exists as a key and password matches
        st.success("Logged In ")
    else:
        st.error('Login Failed')
