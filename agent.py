import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_ollama import OllamaLLM

df = pd.read_excel("sales.csv.xlsx")

llm = OllamaLLM(model="llama3")

agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=True,
    allow_dangerous_code=True
)

question = input("Ask a question about the dataset: ")

result = agent.run(question)

print("Answer:", result)