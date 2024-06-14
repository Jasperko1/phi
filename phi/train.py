import nltk
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
import process
file = open("digest.txt", "r")
content_raw = file.read()
conv = content_raw.split("\n")
usrmsg = conv[::2]
botmsg = conv[1::2]
lem = WordNetLemmatizer()
stop = set(stopwords.words("english"))
for i in range(0, len(usrmsg)):
    if usrmsg and botmsg:
        usr = nltk.word_tokenize(usrmsg[i])
        usr_processed = [lem.lemmatize(token) for token in usr if token.isalpha() and token not in stop]
        usr_fin = [w.upper() for w in usr_processed]
        process.reg(usr_fin, botmsg[i])
    print("Status: "+str(i+1)+"/"+str(len(usrmsg)))
print("Status: FINISHED")
