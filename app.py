import streamlit as st

st.set_page_config(page_title="Fraud Detection App", page_icon="🔍", layout="wide")

st.title("Fraud Detection App")
st.sidebar.success("Select a page bellow.")

st.write("""
Welcome to the **Fraud Detection App**.  
This tool allows you to analyze transactions and predict whether they are fraudulent.  
Use the **sidebar** to navigate between pages.
""")
