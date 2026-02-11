"""
N-gram generation functions for text preprocessing.
"""

from nltk.tokenize import word_tokenize
from nltk.util import ngrams as nltk_ngrams


# Method 1: Generate n-grams from text
def generate_ngrams(text, n=2):
    """
    Generate n-grams from text.

    Args:
        text: Input text string
        n: Size of n-grams (default 2 for bigrams)

    Returns:
        List of n-gram tuples
    """
    tokens = word_tokenize(text.lower())
    n_grams = list(nltk_ngrams(tokens, n))
    return n_grams


# Method 2: Generate n-grams as strings
def generate_ngrams_as_strings(text, n=2, separator=' '):
    """
    Generate n-grams as joined strings.

    Args:
        text: Input text string
        n: Size of n-grams (default 2 for bigrams)
        separator: Character to join n-gram tokens (default space)

    Returns:
        List of n-gram strings
    """
    tokens = word_tokenize(text.lower())
    n_grams = list(nltk_ngrams(tokens, n))
    return [separator.join(gram) for gram in n_grams]


# Method 3: Generate bigrams (2-grams)
def generate_bigrams(text):
    """Generate bigrams from text."""
    return generate_ngrams(text, n=2)


# Method 4: Generate trigrams (3-grams)
def generate_trigrams(text):
    """Generate trigrams from text."""
    return generate_ngrams(text, n=3)


# Method 5: Generate character n-grams
def generate_char_ngrams(text, n=3):
    """
    Generate character-level n-grams from text.

    Args:
        text: Input text string
        n: Size of character n-grams (default 3)

    Returns:
        List of character n-gram tuples
    """
    text = text.lower().replace(' ', '')
    char_ngrams = list(nltk_ngrams(text, n))
    return char_ngrams


# Method 6: Generate n-grams with stopword filtering
def generate_ngrams_no_stopwords(text, stopwords_list, n=2):
    """
    Generate n-grams with stopwords filtered out.

    Args:
        text: Input text string
        stopwords_list: List of stopwords to filter
        n: Size of n-grams (default 2)

    Returns:
        List of n-gram tuples
    """
    tokens = word_tokenize(text.lower())
    filtered_tokens = [token for token in tokens if token.isalnum() and token not in stopwords_list]
    n_grams = list(nltk_ngrams(filtered_tokens, n))
    return n_grams
