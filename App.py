import streamlit as st
from transformers import pipeline
@st.cache_resource
def load_summerize():
  return pipeline("summarization", model="Bocklitz-Lab/lit2vec-tldr-bart-model") 

summerizer = load_summerizer()

st.title("AI Text Summarize")
         st.write("enter a long text below, and get a concise summary!")
long_txt = st.text_area{"enter text to summerize:", height=200)

max_length = st.slider("max summary length", min_value=50, max_value=300, value=130)
min_length = st.slider("min summary length", min_value=20, max_value=100, value=)
if st.button("summarize"):
  if long_text.strip():
    with st.spinner("Generating summary.."):
      summary = summarizer(long_text, max_length=max_length, min_length=min_length, do_sample=false)
      st.subheader("Summary:")
      st.sucess(summary[0]['summary_text'])
  else:
    st.warning("please enter some text to summarize")
