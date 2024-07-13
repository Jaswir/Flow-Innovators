import streamlit as st
import vectara
import langflow_output

st.title("Question and Answer App")

# Reset Corpus Button
if st.button("Reset Corpus"):
    vectara.ResetCorpus()
    st.write("Corpus has been reset.")

# File uploader
st.write("Upload a file to add to the corpus:")
uploaded_file = st.file_uploader("Choose a file", type=["pdf"])

if uploaded_file is not None:
    vectara.AddFile(uploaded_file)
    st.write("File uploaded successfully.")

st.write("Ask a question and get an answer:")

question = st.text_input("Your question:")

if st.button("Get Answer"):
    if question:
        answer = langflow_output.getResponseFromLangFlow(question)
        st.write(answer)
    else:
        st.write("Please enter a question.")
