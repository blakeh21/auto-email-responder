import streamlit as st

# Initialize Streamlit and Gmail configurations
st.write("# Email Tracker")
sidebar = st.sidebar
col1, col2, col3 = st.beta_columns(3)

col1.header("Unread Emails/Follow Ups")
st.write("""
         # Here are unread emails
         This would be email content""")

col2.header("Automation")
st.write("""
         # Here are unread emails
         This would be email content""")

col3.header("Unread Emails")
st.write("""
         # Here are unread emails
         This would be email content""")
