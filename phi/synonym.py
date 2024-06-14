import nltk, random
def getsyn(word):
    syn = []
    for i in nltk.corpus.wordnet.synsets(word):
        for j in i.lemmas():
            syn.append(j.name())
    syn = list(set(syn))
    if not syn:
        out = word
    else:
        out = random.choice(syn)
    return out
