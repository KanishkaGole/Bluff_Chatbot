from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("AIzaSyDAMt1aBItzUwTEGx6-ldPYq7tYy-_e2Bk"))

## function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])

def get_gemini_response(question): 
    response=chat.send_message(question,stream=True)
    return response

def gemr(question):
    # model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(f"Provide brief answer {question}")
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Bluff")

st.header("Bluff")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

response1=""
if submit and input:
    # response1=gemr(f"you are anti addiction therapist bot to answer all sorts of addiction related queries. Only if the given question is not at all relevant to our purpose, then tell user politely that its not related to your purpose and provide them with alternative websites for their question.{input}")
    if gemr(f"does the following question violate gemini's ethical quidelines, answer True or False.{input} ")=="True":
        response=gemr(f"as a therapeutic bot,the user sounds a bit bothered by something so reassure them that you will help them no matter what.")
        response2=gemr(f"{input}")
        response1=(f"{response}\n \n{response2}")
    
    else:
        response1=gemr(f"{input}")


    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("User", input))
    st.subheader("To answer your question..")
    st.write(response1)
    st.session_state['chat_history'].append(("TheBot", response1))
    

    # for chunk in response1:
    #     st.write(chunk.text)
    #     st.session_state['chat_history'].append(("TheBot", chunk.text))

else:
    resp=gemr("Introduce yourself to the user as a empathising therepist bot, \"TheBot\" at Anti-Gambling-Addiction game called \"BLUFF\"")
    st.subheader("About")
    st.write(resp)

st.subheader("\nThe Chat History is")
    
for role, text in st.session_state['chat_history']:
    st.write(f"\n{role}\t: {text}\n\n")
    



    
