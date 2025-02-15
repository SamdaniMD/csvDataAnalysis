# from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent

# from langchain_experimental import create_pandas_dataframe_agent
import pandas as pd
from langchain.llms import OpenAI


def query_agent(data,  query):
    df=pd.read_csv(data)

    llm = OpenAI()

    agent = create_pandas_dataframe_agent(llm, df, verbose=True, allow_dangerous_code=True)
    return agent.run(query)