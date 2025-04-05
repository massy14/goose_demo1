import streamlit as st

def main():
    st.title("🌟 Kid's Learning Assistant 🌟")
    
    # Add a friendly welcome message
    st.write("こんにちは！一緒に楽しく学びましょう！")
    
    # Create a text input for the child's question
    user_input = st.text_input("質問を入力してね！", "")
    
    if user_input:
        # Add some fun responses
        if "こんにちは" in user_input:
            st.write("こんにちは！今日も一緒に楽しく勉強しよう！")
        elif "算数" in user_input:
            st.write("算数は楽しいよ！一緒に考えてみよう！")
        elif "理科" in user_input:
            st.write("自然や科学について学ぶのは面白いね！")
        else:
            st.write("なるほど！それについて一緒に考えてみようか！")
        
        # Add a fun fact section
        st.write("---")
        st.write("📚 今日の豆知識:")
        st.write("宇宙には数え切れないほどの星があるんだ！")

if __name__ == "__main__":
    main()