import streamlit as st
from dotenv import load_dotenv
from utils import query_agent

load_dotenv()

st.title("Lets do some analysis onyour csv file")
st.header("PLease upload your csv file")
# agent = query_agent(allow_dangerous_code=True)

data = st.file_uploader("upload csv file", type="csv")

query= st.text_area("Enter your query")
button=st.button("Generate Reports")

if button:
    answer = query_agent(data, query)
    st.write(answer)