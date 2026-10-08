import streamlit as st
import pandas as pd

st.title("Student Data Dashboard")

uploaded_file = st.file_uploader(
    "Upload an Excel file",
    type=["xlsx"]
)

if uploaded_file is not None:

    df = pd.read_excel(uploaded_file)

    st.subheader("Student Data")

    st.dataframe(df)