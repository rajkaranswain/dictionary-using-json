import json
from difflib import get_close_matches
data = json.load(open("no.1/data.json"))

def translate(w):
    if (w in data):
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yn = input("did you mean %s instead.\nIf yes enter y \n if no press n\n" % get_close_matches(w,data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="n":
            return "word does not exist"
        else:
            return "keys doen't match"           
    else:
        return "word does not exist"  

word= input("enter the word to find:")
word = word.lower()
words = translate(word)
if type(words)== list:
    for item in words:
        print(item)
else:
    print(words)            