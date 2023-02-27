"""This code loads a pandas DataFrame, preprocesses the text data by removing stop words and punctuation, 
then trains a Top2Vec model on the preprocessed text data, and saves the model to a file."""

import pandas as pd
from top2vec import Top2Vec
import nltk
from nltk.corpus import stopwords
import string
from gensim.models import phrases
from gensim.models.phrases import ENGLISH_CONNECTOR_WORDS



# Load the DataFrame
df = pd.read_csv('parec-backend/app/data/reduced_data.csv')

# Create a list of stop words and define punctuation
nltk.download('stopwords')
stop_words = set(stopwords.words('english')) 
punctuation = set(string.punctuation)

# Preprocess the text data by tokenizing, removing stop words, and lowercasing
documents = df['abstract'].tolist()

# Iterate through each string in the documents list
for i, doc in enumerate(documents):
    # Tokenize the string into individual words
    words = nltk.word_tokenize(doc)
    # Filter out the stopwords and punctuation
    words_filtered = [word.lower() for word in words if word.lower() not in stop_words and word not in punctuation]
    # Re-join the filtered words into a single string
    doc_filtered = ' '.join(words_filtered)
    # Replace the original string with the filtered string in the documents list
    documents[i] = doc_filtered

# Train the Top2Vec model
min_count = 5
model = Top2Vec(documents, ngram_vocab=True, ngram_vocab_args = {'min_count': min_count, 'connector_words': phrases.ENGLISH_CONNECTOR_WORDS}, speed='deep-learn', workers=8)

# Save the model to a file
model.save('parec-backend/app/data/t2v_with_n_grams_and_args')

