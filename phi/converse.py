import phi.subject as subject
import phi.generate as generate
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
stop = set(stopwords.words('english'))
open('phi/current.txt', 'w').close()
with open("phi/current.txt", "a+") as g:
    g.write("it can do")
l = WordNetLemmatizer()
while True:
    userinput = input("User: ")
    with open("phi/current.txt", "a+") as f:
        f.seek(0)
        a = f.read()
        if a == "":
            a = "it can do"
        print("Aeona: ",generate.now(userinput, subject.findnow(a)))
        open('phi/current.txt', 'w').close()
        f.write(" ".join([l.lemmatize(userinput) for token in userinput if token.isalpha() and token not in stop]).lower())
