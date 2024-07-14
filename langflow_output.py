from langflow.load import run_flow_from_json
from langflow.graph.schema import RunOutputs
import streamlit as st  
import os

os.environ["OPENAI_API_KEY"]= st.secrets["OPENAI_API_KEY"]
flowname = 'Document QA.json'

def getResponseFromLangFlow(question):
    response = run_flow_from_json(
        flow=flowname,
        input_value=question,
        fallback_to_env_vars=True,  # False by default
    )

    output_text = response[0].outputs[0].results['message'].text
    return output_text

# question = "Background Story: : the student failed the exam, 3 times. Student Experieence: I can understand the topics generally but I can't understand the mathematical formulations, my biggest challenges for the course is to understand mathematical formulations"
question = 'What is the document about?'
result = getResponseFromLangFlow(question)

# print(type(result))
print(result)

