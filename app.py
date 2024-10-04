import streamlit as st
import pandas as pd
from pymongo import MongoClient

page_bg_img = '''
<style>
body {
    background-image: url("https://png.pngtree.com/background/20211215/original/pngtree-modern-simple-elegant-dark-blue-landing-page-website-background-picture-image_1454711.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
'''

# Inject the CSS into the Streamlit app
st.markdown(page_bg_img, unsafe_allow_html=True)
# MongoDB connection
client = MongoClient('mongodb+srv://joelroys637:8838343971leo@cluster0.izjsx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['db1']
collection = db['table1']

# Streamlit app
st.title("Signup, Login, and View Signup Details Page")

# Signup Form
st.header("Signup")
with st.form("signup_form"):
    name = st.text_input("username:")
    email = st.text_input("Enter your email:")
    password = st.text_input("Enter your password:", type="password")
    
    # Submit button for signup
    submitted = st.form_submit_button("Sign Up")

    if submitted:
        if name and email and password:
            # Insert user details into MongoDB
            document = {
                "name": name,
                "email": email,
                "password": password  # In production, ensure to hash the password
            }
            insert_doc = collection.insert_one(document)
            st.success(f"Signup successful! User ID: {insert_doc.inserted_id}")
        else:
            st.error("Please fill out all fields.")

# Login Form
st.header("Login")
with st.form("login_form"):
    login_email = st.text_input("Enter your email for login:")
    login_password = st.text_input("Enter your password for login:", type="password")
    
    # Submit button for login
    login_submitted = st.form_submit_button("Login")

    if login_submitted:
        if login_email and login_password:
            # Check if user exists in MongoDB
            user = collection.find_one({"email": login_email})

            if user:
                # Check if the password matches
                if user["password"] == login_password:  # In production, compare hashed passwords
                    st.success("Login successful!")
                else:
                    st.error("Invalid password. Please try again.")
            else:
                st.error("User not found. Please sign up first.")
        else:
            st.error("Please fill out both email and password fields.")




# Close MongoDB connection
client.close()
