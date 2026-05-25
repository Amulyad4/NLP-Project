from sklearn.feature_extraction.text import TfidfVectorizer

from src.text_cleaning import clean_text


def extract_keywords(text, num_keywords=10):

    cleaned_text = clean_text(text)

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform([cleaned_text])

    feature_names = vectorizer.get_feature_names_out()

    scores = tfidf_matrix.toarray()[0]

    word_scores = {}

    for word, score in zip(feature_names, scores):
        word_scores[word] = score

    sorted_keywords = sorted(
        word_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    keywords = [word for word, score in sorted_keywords[:num_keywords]]

    return keywords