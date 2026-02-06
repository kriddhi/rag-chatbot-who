import streamlit as st
from src.rag_pipeline import ask_rag

st.set_page_config(page_title="MedAssist RAG", page_icon="🩺", layout="wide")

with st.sidebar:
    st.header("ℹ️ About")
    st.write("This assistant answers questions using hospital policies, guidelines, and medical documents.")
    st.write("It does not provide personal medical advice.")

# Custom CSS for nicer chat bubbles
st.markdown("""
<style>
.chat-container {
    max-width: 800px;
    margin: auto;
}
.user-bubble {
    background-color: #DCF8C6;
    padding: 10px 15px;
    border-radius: 15px;
    margin-bottom: 10px;
}
.bot-bubble {
    background-color: #F1F0F0;
    padding: 10px 15px;
    border-radius: 15px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("🩺 MedAssist – Healthcare RAG Assistant")
st.caption("Answers based only on trusted medical documents")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input box at bottom
if prompt := st.chat_input("Ask a healthcare policy or guideline question..."):
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        with st.spinner("🔍 Searching medical knowledge base..."):
            response, sources = ask_rag(prompt)

        st.markdown(response)

        # Show sources
        if sources:
            with st.expander("📚 Sources"):
                for src in sources:
                    st.write(f"- {src}")

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})
