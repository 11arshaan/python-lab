"""
Shared spaCy model loader for the pro subpackage.
"""

import spacy

_nlp = None


def get_nlp(model: str = "en_core_web_sm"):
    """Lazy-load and cache the spaCy model. Returns the shared instance."""
    global _nlp
    if _nlp is None:
        _nlp = spacy.load(model)
    return _nlp
