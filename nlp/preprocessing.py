import nltk
nltk.download('stopwords')
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

en_stopwords = stopwords.words('english')

# Method 1: Simple list comprehension to filter stopwords
def remove_stopwords_simple(text, stopwords_list):
    """Filter out stopwords from text using list comprehension."""
    words = text.split()
    filtered_words = [word for word in words if word not in stopwords_list]
    return ' '.join(filtered_words)

# Method 2: Using tokenized words (more robust)
def remove_stopwords_tokenized(text, stopwords_list):
    """Filter out stopwords from tokenized text."""
    tokens = word_tokenize(text)
    filtered_tokens = [token for token in tokens if token.isalnum() and token not in stopwords_list]
    return ' '.join(filtered_tokens)

# Method 3: Preserve punctuation while filtering stopwords
def remove_stopwords_preserve_punct(text, stopwords_list):
    """Filter stopwords but preserve punctuation."""
    tokens = word_tokenize(text)
    filtered_tokens = [token for token in tokens if token not in stopwords_list]
    return ' '.join(filtered_tokens)
