import streamlit as st
from src.utils import llm_model
import os


# Disable tokenizers parallelism
os.environ["TOKENIZERS_PARALLELISM"] = "false"


# Set page title and description
st.set_page_config(
    page_title="Product Recommendation",
    page_icon=":rocket:",
    layout="wide",
    initial_sidebar_state="auto",
)


# Main title and description
st.title("Product Recommendation")
st.write("Welcome to the Product Recommendation Chatbot. Type your query below.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize chatbot history
chatbot_history = []

# Initialize the chatbot model outside the loop
chatbot = llm_model()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("type your query?"):

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    result = chatbot({"question": prompt, "chat_history": chatbot_history})
    answer = result["answer"]
        
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(answer)
        
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": answer})

   # Append the conversation to the chatbot history
    chatbot_history.append((result["question"], result["answer"]))
    print(chatbot_history)


# Add a section for recommendations or additional content based on the conversation
# Replace the following with your specific recommendations or content logic
st.write("Here are some product recommendations based on your conversation:")

# Add a footer or any additional information
st.sidebar.markdown("### About")
st.sidebar.write(
    "This chatbot provides product recommendations based on your queries. "
    "Please type your questions in the chatbox to get started."
) 

# Add an image to the sidebar
st.sidebar.image("/Users/manjukumari/Downloads/Expected-time-of-delivery.jpg", caption="Product Recommendations")
