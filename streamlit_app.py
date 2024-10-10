import streamlit as st
from transformers import pipeline

text = "Этот курс был создан в партнерстве с Hugging Face."


def translation_ru_en(_input_text):
    translator = pipeline("translation", model="facebook/nllb-200-distilled-600M", src_lang='rus_Cyrl',
                          tgt_lang='eng_Latn')
    translation = translator(_input_text)
    return translation


def translation_en_ru(_input_text):
    translator = pipeline("translation", model="facebook/nllb-200-distilled-600M", src_lang='eng_Latn',
                          tgt_lang='rus_Cyrl')
    translation = translator(_input_text)
    return translation


def translation_ru_fr(_input_text):
    translator = pipeline("translation", model="facebook/nllb-200-distilled-600M", src_lang='rus_Cyrl',
                          tgt_lang='fra_Latn')
    translation = translator(_input_text)
    return translation


st.title("Переводчик текста")

selected_task = st.sidebar.selectbox("Выбрать язык: ",
                                     ["Русский на Английский", "Английский на Русский", "Русский на Французкий"])

input_text = st.text_area("Введите текст:")

if st.button("Перевести"):
    if selected_task == "Русский на Английский" and input_text:
        st.subheader("Перевод:")
        result = translation_ru_en(input_text)
        st.write('', str(result).strip("[{'translation_text': ']}\'"))
    elif selected_task == "Английский на Русский" and input_text:
        st.subheader("Перевод")
        result = translation_en_ru(input_text)
        st.write('', str(result).strip("[{'translation_text': ']}\'"))
    elif selected_task == "Русский на Французкий" and input_text:
        st.subheader("Перевод:")
        result = translation_ru_fr(input_text)
        st.write('', str(result).strip("[{'translation_text': ']}\'"))
    else:
        st.info("Введите текст и выберите задачу на боковой панели.")


