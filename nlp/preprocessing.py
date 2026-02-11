import nltk
nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import PorterStemmer, SnowballStemmer, WordNetLemmatizer
from nltk.tag import pos_tag

en_stopwords = stopwords.words('english')

# Tokenization Functions=================================

# Method 1: Simple list comprehension to filter stopwords, preserving punctuation
def remove_stopwords(text, stopwords_list):
    """Filter out stopwords from text using list comprehension."""
    words = text.split()
    filtered_words = [word for word in words if word not in stopwords_list]
    return ' '.join(filtered_words)

# Method 2: Tokenize text and remove stopwords and punctuation
def tokenize(text, stopwords_list):
    """Filter out stopwords from tokenized text."""
    tokens = word_tokenize(text)
    filtered_tokens = [token for token in tokens if token.isalnum() and token not in stopwords_list]
    return ' '.join(filtered_tokens)

# Method 3: Tokenize text and remove stopwords, preserve punctuation
def tokenize_with_punct(text, stopwords_list):
    """Filter stopwords but preserve punctuation."""
    tokens = word_tokenize(text)
    filtered_tokens = [token for token in tokens if token not in stopwords_list]
    return ' '.join(filtered_tokens)

# Stemming Functions====================================

# Method 1: Porter Stemmer (standard English stemming)
def stem_porter(text):
    """Apply Porter Stemmer to reduce words to their root form."""
    stemmer = PorterStemmer()
    tokens = word_tokenize(text)
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return ' '.join(stemmed_tokens)

# Method 2: Snowball Stemmer (supports multiple languages)
def stem_snowball(text, language='english'):
    """Apply Snowball Stemmer to reduce words to their root form."""
    stemmer = SnowballStemmer(language)
    tokens = word_tokenize(text)
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return ' '.join(stemmed_tokens)

# Method 3: Combine stopword removal and stemming
def tokenize_and_stem(text, stopwords_list):
    """Remove stopwords and apply Porter Stemmer in one step."""
    stemmer = PorterStemmer()
    tokens = word_tokenize(text.lower())
    processed_tokens = [
        stemmer.stem(token)
        for token in tokens
        if token.isalnum() and token not in stopwords_list
    ]
    return ' '.join(processed_tokens)

# Lemmatization Functions====================================

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
    pos_tags = pos_tag(tokens) #generate POS tags for each token

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
