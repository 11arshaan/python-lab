"""
NLP preprocessing package for tokenization, stemming, lemmatization, and n-gram generation.
"""

# Import tokenization functions
from .tokenization import (
    remove_stopwords,
    tokenize,
    tokenize_with_punct,
    tokenize_sentences,
    tokenize_words,
    en_stopwords
)

# Import stemming functions
from .stemming import (
    stem_porter,
    stem_snowball,
    tokenize_and_stem
)

# Import lemmatization functions
from .lemmatization import (
    lemmatize_basic,
    lemmatize_with_pos,
    tokenize_and_lemmatize,
    get_wordnet_pos
)

# Import n-gram functions
from .ngrams import (
    generate_ngrams,
    generate_ngrams_as_strings,
    generate_bigrams,
    generate_trigrams,
    generate_char_ngrams,
    generate_ngrams_no_stopwords
)

__all__ = [
    # Tokenization
    'remove_stopwords',
    'tokenize',
    'tokenize_with_punct',
    'tokenize_sentences',
    'tokenize_words',
    'en_stopwords',
    # Stemming
    'stem_porter',
    'stem_snowball',
    'tokenize_and_stem',
    # Lemmatization
    'lemmatize_basic',
    'lemmatize_with_pos',
    'tokenize_and_lemmatize',
    'get_wordnet_pos',
    # N-grams
    'generate_ngrams',
    'generate_ngrams_as_strings',
    'generate_bigrams',
    'generate_trigrams',
    'generate_char_ngrams',
    'generate_ngrams_no_stopwords',
]
