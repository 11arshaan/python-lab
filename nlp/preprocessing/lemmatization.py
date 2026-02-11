"""
Lemmatization functions for text preprocessing using WordNet.
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag

# Download required NLTK data
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)


# Helper function to convert nltk pos tags to wordnet pos tags
def get_wordnet_pos(treebank_tag):
    """Convert treebank POS tags to wordnet POS tags."""
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


# Method 1: Basic lemmatization (no POS tagging)
def lemmatize_basic(text):
    """Apply WordNetLemmatizer to reduce words to their base form."""
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text.lower())
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(lemmatized_tokens)


# Method 2: Lemmatization with POS tagging (more accurate)
def lemmatize_with_pos(text):
    """Apply lemmatization with part-of-speech tagging for better accuracy."""
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text.lower())
    pos_tags = pos_tag(tokens)  # generate POS tags for each token

    lemmatized_tokens = []
    for token, pos in pos_tags:
        wordnet_pos = get_wordnet_pos(pos)
        if wordnet_pos:
            lemmatized_tokens.append(lemmatizer.lemmatize(token, pos=wordnet_pos))
        else:
            lemmatized_tokens.append(lemmatizer.lemmatize(token))

    return ' '.join(lemmatized_tokens)


# Method 3: Combine stopword removal and lemmatization
def tokenize_and_lemmatize(text, stopwords_list):
    """Remove stopwords and apply lemmatization in one step."""
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text.lower())
    pos_tags = pos_tag(tokens)

    processed_tokens = []
    for token, pos in pos_tags:
        if token.isalnum() and token not in stopwords_list:
            wordnet_pos = get_wordnet_pos(pos)
            if wordnet_pos:
                processed_tokens.append(lemmatizer.lemmatize(token, pos=wordnet_pos))
            else:
                processed_tokens.append(lemmatizer.lemmatize(token))

    return ' '.join(processed_tokens)
