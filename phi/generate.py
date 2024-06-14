import nltk, re, phi.sentiment as sentiment, random
stop = set(nltk.corpus.stopwords.words("english"))
lem = nltk.stem.WordNetLemmatizer()
def now(userinput, subject):
    userinput_new = userinput
    userinput_new = userinput_new.replace(".","#")
    userinput_new = userinput_new.replace(",","#")
    userinput_new = userinput_new.replace(":","#")
    userinput_new = userinput_new.replace(";","#")
    userinput_new = userinput_new.replace("?","#")
    userinput_new = userinput_new.replace("!","#")
    usinp = userinput_new.split("#")
    usin = []
    for item in usinp:
        if item.startswith(" ") and item.endswith(" "):
            usin.append(item[1:-1])
        elif item.startswith(" "):
            usin.append(item[1:])
        elif item.endswith(" "):
            usin.append(item[:-1])
        else:
            usin.append(item)
    usi = [item for item in usin if item != '']
    score = sentiment.emotionscore(subject.capitalize()+". "+"".join(userinput))
    sentence_list = []
    generated_list = []
    if score < -0.25:
        generated_list.append("Aww, that's bad.")
    elif score >= 0.25:
        generated_list.append("Great!")
    else:
        pass
    for sentence in usi:
        i = nltk.word_tokenize(sentence)
        i = " ".join([lem.lemmatize(k) for k in i if k.isalpha() and k not in stop])
        sentence_list.append(i)
        file = open("phi/data.txt","r")
        content_raw = file.read()
    for this in range(0,len(sentence_list)):
        sentence_each = []
        for l in sentence_list:
            a = l.upper()
        matches = re.finditer(a, content_raw)
        positions = [match.end() for match in matches if match.group(0).isupper()]
        for that in range(0,len(positions)):
            if content_raw[positions[that] - 1].isalpha() or content_raw[positions[that] + 1].isalpha():
                pass
            those = content_raw.find("#", positions[that])+1
            these = content_raw.find("]", positions[that])
            if these == -1:
                pass
            sentence_each.append(content_raw[those:these])
        if sentence_each:
            generated_list.append(random.choice(sentence_each))
    if not generated_list:
        generated_list.append("Okay.")
    return " ".join(generated_list)
