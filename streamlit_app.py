import streamlit as st
from transformers import pipeline

text = "Этот курс был создан в партнерстве с Hugging Face."


def translate(_input_text, _src_lang, _tgt_lang):
    translator = pipeline("translation", model="facebook/nllb-200-distilled-600M",
                          src_lang=_src_lang, tgt_lang=_tgt_lang)
    translation = translator(_input_text)
    return translation


st.title("Переводчик текста")

selected_task = st.sidebar.selectbox("Выбрать язык: ",
                                     ["Русский на Английский", "Английский на Русский", "Русский на Французкий"])

input_text = st.text_area("Введите текст:")

if st.button("Перевести"):
    st.subheader("Перевод:")
    if selected_task == "Русский на Английский" and input_text:
        result = translate(input_text, 'rus_Cyrl', 'eng_Latn')
        st.write('', str(result).strip("[{'translation_text': ']}\'"))
    elif selected_task == "Английский на Русский" and input_text:
        result = translate(input_text, 'eng_Latn', 'rus_Cyrl')
        st.write('', str(result).strip("[{'translation_text': ']}\'"))
    elif selected_task == "Русский на Французкий" and input_text:
        result = translate(input_text, 'rus_Cyrl', 'fra_Latn')
        st.write('', str(result).strip("[{'translation_text': ']}\'"))
    else:
        st.info("Введите текст и выберите задачу на боковой панели.")

