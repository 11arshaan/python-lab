"""
Educational NLP preprocessing functions (NLTK-based).

Provides tokenization, stemming, lemmatization, and n-gram generation
using NLTK for learning and experimentation.
"""

from .tokenization import (
    remove_stopwords,
    tokenize,
    tokenize_with_punct,
    tokenize_sentences,
    tokenize_words,
    en_stopwords,
)

from .stemming import (
    stem_porter,
    stem_snowball,
    tokenize_and_stem,
)

from .lemmatization import (
    lemmatize_basic,
    lemmatize_with_pos,
    tokenize_and_lemmatize,
    get_wordnet_pos,
)

from .ngrams import (
    generate_ngrams,
    generate_ngrams_as_strings,
    generate_bigrams,
    generate_trigrams,
    generate_char_ngrams,
    generate_ngrams_no_stopwords,
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
