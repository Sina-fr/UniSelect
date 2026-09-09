"""
UniSelect Streamlit application.

Provides a simple web interface for uploading an Excel-based unit selection
table, previewing its contents, and saving it to the local data directory.
"""

import os

import pandas as pd
import streamlit as st

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
os.makedirs(DATA_DIR, exist_ok=True)


def main():
    """Run the UniSelect Streamlit page for uploading and saving unit selection tables.

    Allows the user to upload an Excel file, preview it in the browser, and
    persist it to the project's data directory.
    """
    st.title("UviSelect")

    uploaded_file = st.file_uploader("Unit selection table", type=["xlsx", "xls"])

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.subheader("Preview")
        st.dataframe(df)

        if st.button("Save to data directory"):
            save_path = os.path.join(DATA_DIR, uploaded_file.name)
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"File saved to {save_path}")


if __name__ == "__main__":
    main()
