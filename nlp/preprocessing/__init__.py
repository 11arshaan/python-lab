"""
NLP preprocessing package for tokenization, stemming, lemmatization,
n-gram generation, and named entity recognition.

Subpackages:
    edu - Educational implementations using NLTK
    pro - Production implementations using spaCy

For backward compatibility, all edu (NLTK) functions are re-exported
at this level. Use subpackage imports for explicit selection:

    from nlp.preprocessing.edu import tokenize_and_lemmatize  # NLTK
    from nlp.preprocessing.pro import tokenize_and_lemmatize  # spaCy
    from nlp.preprocessing import tokenize_and_lemmatize      # NLTK (backward compat)
"""

# Backward-compatible re-exports from edu
from .edu import (
    # Tokenization
    remove_stopwords,
    tokenize,
    tokenize_with_punct,
    tokenize_sentences,
    tokenize_words,
    en_stopwords,
    # Stemming
    stem_porter,
    stem_snowball,
    tokenize_and_stem,
    # Lemmatization
    lemmatize_basic,
    lemmatize_with_pos,
    tokenize_and_lemmatize,
    get_wordnet_pos,
    # N-grams
    generate_ngrams,
    generate_ngrams_as_strings,
    generate_bigrams,
    generate_trigrams,
    generate_char_ngrams,
    generate_ngrams_no_stopwords,
)

# Make subpackages importable
from . import edu
from . import pro

__all__ = [
    # Subpackages
    'edu',
    'pro',
    # Tokenization (backward compat from edu)
    'remove_stopwords',
    'tokenize',
    'tokenize_with_punct',
    'tokenize_sentences',
    'tokenize_words',
    'en_stopwords',
    # Stemming (backward compat from edu)
    'stem_porter',
    'stem_snowball',
    'tokenize_and_stem',
    # Lemmatization (backward compat from edu)
    'lemmatize_basic',
    'lemmatize_with_pos',
    'tokenize_and_lemmatize',
    'get_wordnet_pos',
    # N-grams (backward compat from edu)
    'generate_ngrams',
    'generate_ngrams_as_strings',
    'generate_bigrams',
    'generate_trigrams',
    'generate_char_ngrams',
    'generate_ngrams_no_stopwords',
]
