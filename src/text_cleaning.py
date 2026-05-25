import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def clean_text(text):
    # lowercase
    text = text.lower()

    # remove numbers
    text = re.sub(r'\d+', '', text)

    # remove punctuation/special chars
    text = re.sub(r'[^\w\s]', '', text)

    # tokenize
    words = word_tokenize(text)

    # remove stopwords + lemmatization
    cleaned_words = []

    for word in words:
        if word not in stop_words:
            lemma_word = lemmatizer.lemmatize(word)
            cleaned_words.append(lemma_word)

    return " ".join(cleaned_words)