import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
### function for NLP

def text_trans(text):
  text = text.lower()
  text = nltk.word_tokenize(text)

  y = []
  for i in text:
    if i.isalnum():
      y.append(i)
  text = y[:]
  y.clear()
  for i in text:
    if i not in stopwords.words("english") and i not in string.punctuation:
      y.append(i)
  text = y[:]
  y.clear()

  for i in text:
    y.append(ps.stem(i))

  return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email And SMS Spam Classifier")

input_sms = st.text_area("Enter Your Message")

if st.button("Predict"):
    # 1. preprocess
    tranformed_sms = text_trans(input_sms)
    # 2. vectorize
    vecto_input = tfidf.transform([tranformed_sms])
    # 3. predict
    result = model.predict(vecto_input)[0]
    # 4. Dsiplay
    if result ==1:
        st.header("SPAM")
    else:
        st.header("NOT SPAM")