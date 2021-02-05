from utils.noise_removal import remove_noise
from utils.lemmatization import lemmatize_it

sentence = input()

def text_processing(sentence):
    sentence1 = remove_noise(sentence)
    return lemmatize_it(sentence1)

print(text_processing(sentence))
