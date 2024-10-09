import streamlit as st
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast, pipeline, AutoTokenizer

article_en = "Once the examples are prepared in this format, it can be trained as any other sequence-to-sequence model."
article_ka = "После подготовки примеров в этом формате их можно обучать так же, как и любую другую модель «последовательность-последовательность»."

model_name = "facebook/mbart-large-50-many-to-many-mmt"


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def download_model():
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer


st.title('Hindi to English Translater')
text = st.text_area("Enter Text:", value='', height=None, max_chars=None, key=None)
model, tokenizer = download_model()

if st.button('Translate to English'):
    if text == '':
        st.write('Please enter Hindi text for translation')
    else:
        # Перевести Английский на Японский
        tokenizer.src_lang = "en_XX"  #@param {type:"string"}
        lang1 = "ja_XX"  #@param {type:"string"}
        encoded_hi = tokenizer(article_en, return_tensors="pt")
        generated_tokens = model.generate(**encoded_hi,
                                          forced_bos_token_id=tokenizer.lang_code_to_id[lang1])
        out = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        st.write('', str(out).strip('][\''))
        # => サンプルがこの形式で準備されると、他のシーケンスからシーケンスモデルとして訓練することができます。

else:
    pass

# # Перевести Русский на Казахский язык
# tokenizer.src_lang = "ru_RU"  #@param {type:"string"}
# lang2 = "kk_KZ"  #@param {type:"string"}
# encoded_ar = tokenizer(article_ka, return_tensors="pt")
# generated_tokens = model.generate(**encoded_ar,
#                                   forced_bos_token_id=tokenizer.lang_code_to_id[lang2])
# st.write(tokenizer.batch_decode(generated_tokens, skip_special_tokens=True))
# # => Үздіктер preparedша, олар басқа модельді «шеңдік-шеңдік» деп үйретуге болады.
