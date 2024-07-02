import streamlit as st

def analyze_text(text):
    words = len(text.split())
    characters = len(text)
    sentences = text.count('.') + text.count('?') + text.count('!')
    paragraphs = text.count('nn') + 1
    return words, characters, sentences, paragraphs

st.title('Анализатор текста')
text = st.text_area('Введите ваш текст здесь:', height=200)

if st.button('Анализировать'):
    words, characters, sentences, paragraphs = analyze_text(text)
    st.write(f'Количество слов: {words}')
    st.write(f'Количество символов: {characters}')
    st.write(f'Количество предложений: {sentences}')
    st.write(f'Количество абзацев: {paragraphs}')
