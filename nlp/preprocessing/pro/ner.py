"""
Named Entity Recognition functions using spaCy.
"""

from spacy import displacy
from spacy.glossary import explain

from ._model import get_nlp


def extract_entities(text: str) -> list[tuple[str, str]]:
    """Extract named entities from text.

    Returns:
        List of (entity_text, entity_label) tuples.
        Example: [("Google", "ORG"), ("Larry Page", "PERSON")]
    """
    doc = get_nlp()(text)
    return [(ent.text, ent.label_) for ent in doc.ents]


def extract_entities_by_label(text: str, label: str) -> list[str]:
    """Extract named entities of a specific type.

    Args:
        text: Input text string.
        label: Entity label to filter by (e.g., "PERSON", "ORG", "DATE").

    Returns:
        List of entity text strings matching the label.
    """
    doc = get_nlp()(text)
    return [ent.text for ent in doc.ents if ent.label_ == label]


def extract_entities_detailed(text: str) -> list[dict]:
    """Extract named entities with detailed information.

    Returns:
        List of dicts with keys: text, label, start_char, end_char, description.
    """
    doc = get_nlp()(text)
    return [
        {
            "text": ent.text,
            "label": ent.label_,
            "start_char": ent.start_char,
            "end_char": ent.end_char,
            "description": explain(ent.label_),
        }
        for ent in doc.ents
    ]


def render_entities_html(text: str) -> str:
    """Render named entities as HTML using displaCy.

    Useful for displaying in Jupyter notebooks via IPython.display.HTML.

    Returns:
        HTML string with entity highlighting.
    """
    doc = get_nlp()(text)
    return displacy.render(doc, style="ent", jupyter=False)
