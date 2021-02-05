from nltk.stem.wordnet import WordNetLemmatizer 
lem = WordNetLemmatizer()

def lemmatize_it(sentence):
    return lem.lemmatize(sentence, "v")
    