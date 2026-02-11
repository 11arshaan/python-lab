"""
Production tokenization functions using spaCy.
"""

from spacy.lang.en.stop_words import STOP_WORDS

from ._model import get_nlp

# spaCy's built-in English stopwords
en_stopwords = STOP_WORDS


def remove_stopwords(text: str) -> str:
    """Remove stopwords from text using spaCy's built-in stop word list."""
    doc = get_nlp()(text)
    filtered = [token.text for token in doc if not token.is_stop]
    return " ".join(filtered)


def tokenize(text: str) -> str:
    """Tokenize text, removing stopwords and punctuation."""
    doc = get_nlp()(text)
    filtered = [
        token.text for token in doc
        if not token.is_stop and not token.is_punct and not token.is_space
    ]
    return " ".join(filtered)


def tokenize_with_punct(text: str) -> str:
    """Tokenize text, removing stopwords but keeping punctuation."""
    doc = get_nlp()(text)
    filtered = [token.text for token in doc if not token.is_stop]
    return " ".join(filtered)


def tokenize_sentences(text: str) -> list[str]:
    """Split text into sentences using spaCy's sentence boundary detector."""
    doc = get_nlp()(text)
    return [sent.text.strip() for sent in doc.sents]


def tokenize_words(text: str) -> list[str]:
    """Split text into word tokens."""
    doc = get_nlp()(text)
    return [token.text for token in doc]
