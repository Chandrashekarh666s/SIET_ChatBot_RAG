Behave As a ML And Agent Specialist , who have built beginner to advanced agents workflows and language understanding . Have an experience about 10 years. MY level is complete beginner - 0% , I have only 2-3 hours in a day . For that i have to manage DSA(Python) , Next the concepts which i am going to feed in the chat(ML, LLM, RAG , Agentic AI ....) Plan for my tier-1 product based company . The information or the resource which you will give must have proper impact and make difference. By following it i need to develop a problem-solving , critical-thinking mentality. i need to develop a Founder-CEO mindset. Explain how to analyse the senario. finally  i must have the capability to crack the technical-interviews and rounds. Plan for 3-months(non-negotiable) plan. I must have the capability to be odd in this society and be aware of -99% mentality. Give me the topics , consistant-plan by understanding my mentality. How to manage EQ state in such situations. 

import stramlit as st
import rag_engine import load_base, ask_rag
st.set_page.config(page_title = "SIET_CHATBOT", layout = "centered")
st.title("Shridevi Institute of Engineering and Technology - ChatBot")
st.caption("Ask anything about the college information")
st.caption("Created by Chandrashekar H")

mykey = st.secrets("GROQ_API_KEY")
@st.cache_resource #Reducing overloading 
def intiate_rag():
  return load_base("01_College_Information.pdf")
index, embd_model, chunks = initiate.rag()

if "chat_hist" not in st.session_state:
  st.session_state.chat_hist = []

for qa in st.session_state.chat_hist:
  with st.chat_message(qa["role"]):
    st.write(qa["content"])
    


question = st.chat_input("Ask anything about SIET college....")

if question:
  st.session_state.chat_hist.append (
    {"role" : "user" , content = question})
  with st.chat_message("user"):
    st.write(question)

  with st.chat_message("assistant"):
    with st.spinner("Asking RAG for answer....."):
      answer = ask_rag(question , embd_model , chunks , index , api_key =mykey , num_chunks)
      st.write(answer)

if st.button("Clear chat"):
  st.session_state.chat_hist = []
  st.rerun()

