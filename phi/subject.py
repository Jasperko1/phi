from nltk.corpus import wordnet
def findnow(context):
    noun = "it"
    verb = "do"
    determine = "can"
    e = context.split(" ")
    e.reverse()
    for i in e:
        if wordnet.synsets(i):
            if wordnet.synsets(i)[0].pos() == "n":
                noun = i
                break
    for j in e:
        k = 0
        if wordnet.synsets(j):
            if wordnet.synsets(j)[0].pos() == "v":
                verb = i
                k = 1
                continue
        if k == 1:
            if "not" or "n't" in j:
                determine = "can't"
            break
    return noun + " " + determine + " " + verb
