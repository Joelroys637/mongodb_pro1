import streamlit as st
import pandas as pd
from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb+srv://joelroys637:8838343971leo@cluster0.izjsx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['db1']
collection = db['table1']



# View Signup Details
st.header("View Signup Details")
if st.button("Show Signup Details"):
    # Retrieve all signup data from MongoDB
    users = list(collection.find({}, {"_id": 0, "name": 1, "email": 1}))  # Exclude password and _id for privacy
    if users:
        # Convert to DataFrame
        df = pd.DataFrame(users)
        # Display the DataFrame in Streamlit
        st.dataframe(df)
    else:
        st.write("No users found.")
        
# Close MongoDB connection
client.close()