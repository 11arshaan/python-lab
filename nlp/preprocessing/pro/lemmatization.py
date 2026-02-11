"""
Production lemmatization functions using spaCy.

spaCy performs POS-aware lemmatization by default as part of its
pipeline, so all functions here produce POS-informed lemmas.
"""

from ._model import get_nlp


def lemmatize(text: str) -> str:
    """Lemmatize text using spaCy's built-in POS-aware lemmatizer.

    Equivalent to edu's lemmatize_with_pos -- spaCy always uses POS
    context for lemmatization.
    """
    doc = get_nlp()(text)
    return " ".join(token.lemma_ for token in doc)


def tokenize_and_lemmatize(text: str) -> str:
    """Remove stopwords, punctuation, and lemmatize in one step.

    Equivalent to edu's tokenize_and_lemmatize(text, stopwords_list),
    but uses spaCy's built-in stopword detection (no list needed).
    """
    doc = get_nlp()(text.lower())
    processed = [
        token.lemma_ for token in doc
        if not token.is_stop and not token.is_punct
        and not token.is_space and token.is_alpha
    ]
    return " ".join(processed)


def get_pos_tags(text: str) -> list[tuple[str, str]]:
    """Return Universal POS tags for each token.

    Replaces edu's get_wordnet_pos helper -- spaCy provides POS tags
    directly without needing tag-system conversion.

    Returns:
        List of (token_text, pos_tag) tuples.
    """
    doc = get_nlp()(text)
    return [(token.text, token.pos_) for token in doc]
