import streamlit as st
import ollama

def init_chat_history():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def get_llm_response(prompt):
    try:
        response = ollama.chat(
            model='gemma3:1b',
            messages=[{'role': 'user', 'content': prompt}],
            stream=False
        )
        return response['message']['content']
    except Exception as e:
        st.error(f"エラーが発生しました: {str(e)}")
        return None

def main():
    st.title("🌟 Kid's Learning Assistant 🌟")
    
    # Initialize chat history
    init_chat_history()
    
    # Add a friendly welcome message
    st.write("こんにちは！一緒に楽しく学びましょう！")
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Create a text input for the child's question
    if prompt := st.chat_input("質問を入力してね！"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get and display assistant response
        with st.chat_message("assistant"):
            response = get_llm_response(prompt)
            if response:
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()