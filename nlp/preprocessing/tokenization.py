"""
Tokenization and stopword filtering functions for text preprocessing.
"""

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

# Download required NLTK data
nltk.download('stopwords', quiet=True)
nltk.download('punkt_tab', quiet=True)

# Load English stopwords
en_stopwords = stopwords.words('english')


# Method 1: Simple list comprehension to filter stopwords, preserving punctuation
def remove_stopwords(text, stopwords_list):
    """Filter out stopwords from text using list comprehension."""
    words = text.split()
    filtered_words = [word for word in words if word not in stopwords_list]
    return ' '.join(filtered_words)


# Method 2: Tokenize text and remove stopwords and punctuation
def tokenize(text, stopwords_list):
    """Filter out stopwords from tokenized text."""
    tokens = word_tokenize(text)
    filtered_tokens = [token for token in tokens if token.isalnum() and token not in stopwords_list]
    return ' '.join(filtered_tokens)


# Method 3: Tokenize text and remove stopwords, preserve punctuation
def tokenize_with_punct(text, stopwords_list):
    """Filter stopwords but preserve punctuation."""
    tokens = word_tokenize(text)
    filtered_tokens = [token for token in tokens if token not in stopwords_list]
    return ' '.join(filtered_tokens)


# Sentence tokenization
def tokenize_sentences(text):
    """Split text into sentences."""
    return sent_tokenize(text)


# Word tokenization only (no filtering)
def tokenize_words(text):
    """Split text into word tokens."""
    return word_tokenize(text)
