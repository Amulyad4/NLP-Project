from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict
import heapq

from src.text_cleaning import clean_text


def generate_summary(text, num_sentences=3):

    # Clean text
    cleaned_text = clean_text(text)

    # Tokenize cleaned words
    words = word_tokenize(cleaned_text)

    # Create word frequency table
    word_frequencies = defaultdict(int)

    for word in words:
        word_frequencies[word] += 1

    # Normalize frequencies
    max_frequency = max(word_frequencies.values())

    for word in word_frequencies:
        word_frequencies[word] /= max_frequency

    # Original sentences
    sentences = sent_tokenize(text)

    # Sentence scores
    sentence_scores = defaultdict(float)

    for sentence in sentences:

        sentence_words = word_tokenize(sentence.lower())

        # Balanced sentence filtering
        if 5 < len(sentence_words) < 60:

            for word in sentence_words:

                if word in word_frequencies:
                    sentence_scores[sentence] += word_frequencies[word]

    # Get top ranked sentences
    summary_sentences = heapq.nlargest(
        num_sentences,
        sentence_scores,
        key=sentence_scores.get
    )

    # Preserve original order
    summary_sentences = sorted(
        summary_sentences,
        key=lambda s: sentences.index(s)
    )

    # Final summary
    summary = " ".join(summary_sentences)

    return summary