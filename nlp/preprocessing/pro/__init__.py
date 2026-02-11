"""
Production NLP preprocessing functions (spaCy-based).

Provides tokenization, lemmatization, and named entity recognition
using spaCy for production-quality text processing.

Requires: python -m spacy download en_core_web_sm
"""

from .tokenization import (
    remove_stopwords,
    tokenize,
    tokenize_with_punct,
    tokenize_sentences,
    tokenize_words,
    en_stopwords,
)

from .lemmatization import (
    lemmatize,
    tokenize_and_lemmatize,
    get_pos_tags,
)

from .ner import (
    extract_entities,
    extract_entities_by_label,
    extract_entities_detailed,
    render_entities_html,
)

__all__ = [
    # Tokenization
    'remove_stopwords',
    'tokenize',
    'tokenize_with_punct',
    'tokenize_sentences',
    'tokenize_words',
    'en_stopwords',
    # Lemmatization
    'lemmatize',
    'tokenize_and_lemmatize',
    'get_pos_tags',
    # NER
    'extract_entities',
    'extract_entities_by_label',
    'extract_entities_detailed',
    'render_entities_html',
]
