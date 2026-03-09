import streamlit as st
import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_ollama import OllamaLLM

# Title
st.title("StatBot Pro - Autonomous CSV Data Analyst")

st.write("Upload a CSV or Excel file and ask questions about your data.")

# File uploader
uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:

    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Dataset preview
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Dataset info
    st.subheader("Dataset Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    st.write("Column Names:")
    st.write(df.columns.tolist())

    # Statistics
    if len(df.select_dtypes(include="number").columns) > 0:
        st.subheader("Basic Statistics")
        st.write(df.describe())

    # Chart section
    st.subheader("Data Visualization")

    numeric_columns = df.select_dtypes(include="number").columns

    if len(numeric_columns) > 0:
        selected_column = st.selectbox(
            "Select numeric column for chart",
            numeric_columns
        )

        st.bar_chart(df[selected_column])

    # Ask questions
    st.subheader("Ask Questions About Your Data")

    question = st.text_input("Ask a question about your dataset")

    if question:

        llm = OllamaLLM(model="llama3")

        agent = create_pandas_dataframe_agent(
            llm,
            df,
            verbose=True,
            allow_dangerous_code=True
        )

        with st.spinner("Analyzing data..."):
            result = agent.run(question)

        st.subheader("Answer")
        st.write(result)