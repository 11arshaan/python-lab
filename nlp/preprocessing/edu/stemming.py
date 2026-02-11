"""
Stemming functions for text preprocessing.
"""

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer


# Method 1: Porter Stemmer (standard English stemming)
def stem_porter(text):
    """Apply Porter Stemmer to reduce words to their root form."""
    stemmer = PorterStemmer()
    tokens = word_tokenize(text)
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return ' '.join(stemmed_tokens)


# Method 2: Snowball Stemmer (supports multiple languages)
def stem_snowball(text, language='english'):
    """Apply Snowball Stemmer to reduce words to their root form."""
    stemmer = SnowballStemmer(language)
    tokens = word_tokenize(text)
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return ' '.join(stemmed_tokens)


# Method 3: Combine stopword removal and stemming
def tokenize_and_stem(text, stopwords_list):
    """Remove stopwords and apply Porter Stemmer in one step."""
    stemmer = PorterStemmer()
    tokens = word_tokenize(text.lower())
    processed_tokens = [
        stemmer.stem(token)
        for token in tokens
        if token.isalnum() and token not in stopwords_list
    ]
    return ' '.join(processed_tokens)
