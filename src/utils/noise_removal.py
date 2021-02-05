from nltk.corpus import stopwords
en_stops = set(stopwords.words('english'))

def remove_noise(sentence):
    words = sentence.split() 
    noise_free_words = [word for word in words if word not in en_stops] 
    noise_free_text = " ".join(noise_free_words) 
    return noise_free_text
    print("worked")