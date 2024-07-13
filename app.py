import streamlit as st
import langflow_output

st.title("Question and Answer App")

st.write("Ask a question and get an answer:")

question = st.text_input("Your question:")

if st.button("Get Answer"):
    if question:
        answer = langflow_output.getResponseFromLangFlow(question)
        st.write(answer)
    else:
        st.write("Please enter a question.")


