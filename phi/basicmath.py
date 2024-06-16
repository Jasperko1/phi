def returnvalue(sentence):
    sentence_r = sentence.lower()
    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    scales = ["hundred", "thousand", "million", "billion", "trillion"]
    symbolized = sentence_r.replace(" ", "#")
    symbolized = symbolized.replace("plus", "+")
    symbolized = symbolized.replace("added to", "+")
    symbolized = symbolized.replace("minus", "-")
    symbolized = symbolized.replace("subtracted#by", "-")
    symbolized = symbolized.replace("subtracted#from", "~")
    symbolized = symbolized.replace("divided#by", "/")
    symbolized = symbolized.replace("divide", "/")
    symbolized = symbolized.replace("times", "*")
    symbolized = symbolized.replace("multiplied#by", "*")
    symbolized = symbolized.replace("and#", "")
    for i in range(1, len(symbolized) - 1):
        if symbolized[i] == "-" and symbolized[i-1].isalpha() and symbolized[i+1].isalpha():
            symbolized = symbolized[:i] + "#" + symbolized[i+1:]
    for i in range(1, len(symbolized) - 1):
        if symbolized[i] == "-" and symbolized[i-1].isnumeric() and symbolized[i+1].isnumeric():
            symbolized = symbolized[:i] + "#-#" + symbolized[i+1:]
    for i in range(1, len(symbolized) - 1):
        if symbolized[i] == "+" and symbolized[i-1].isnumeric() and symbolized[i+1].isnumeric():
            symbolized = symbolized[:i] + "#+#" + symbolized[i+1:]
    for i in range(1, len(symbolized) - 1):
        if symbolized[i] == "*" and symbolized[i-1].isnumeric() and symbolized[i+1].isnumeric():
            symbolized = symbolized[:i] + "#*#" + symbolized[i+1:]
    for i in range(1, len(symbolized) - 1):
        if symbolized[i] == "/" and symbolized[i-1].isnumeric() and symbolized[i+1].isnumeric():
            symbolized = symbolized[:i] + "#/#" + symbolized[i+1:]
    oplist = []
    strinlist = ""
    rawstr = symbolized.split("#")
    rawstr.append("")
    for word in rawstr:
        if word.isalnum():
            strinlist += word + " "
        else:
            oplist.append(strinlist)
            oplist.append(word)
            strinlist = ""
    for item in range(len(oplist)):
        if oplist[item].endswith(" "):
            oplist[item] = oplist[item][:-1]
    oplist.pop()
    for indexed in range(0, len(oplist)):
        item = oplist[indexed]
        if item == "+" or item == "-" or item == "~" or item == "/" or item == "*":
            continue
        itemlist = item.split(" ")
        convert_raw = []
        for conv in itemlist:
            if conv in units:
                convert_raw.append(units.index(conv))
            elif conv in tens:
                 convert_raw.append(tens.index(conv)*10)
            elif conv in scales:
                if "e" in conv:
                    convert_raw.append(100)
                elif "s" in conv:
                    convert_raw.append(1000)
                elif "m" in conv:
                    convert_raw.append(1000000)
                elif "b" in conv:
                    convert_raw.append(1000000000)
                else:
                    convert_raw.append(1000000000000)
            else:
                pass
        conv_num = 0
        temp_num = 1
        curr_num = 1
        for i in convert_raw:
            if i >= curr_num:
                temp_num *= i
                curr_num = i
            else:
                curr_num = i
                conv_num += temp_num + curr_num
                temp_num = curr_num = 1
            if len(convert_raw) == 1:
                conv_num = temp_num
            if itemlist in units:
                conv_num = "".join([units[w] for w in itemlist])
            oplist[indexed] = str(conv_num)
    for m in range(0, len(oplist)):
        if oplist[m] == "~":
            oplist[m] = "-"
            oplist = oplist[m+1:] + ["-"] + oplist[:m]
    try:
        return str(eval("".join(oplist)))
    except NameError:
        return "invalid"
    except SyntaxError:
        return "invalid"
