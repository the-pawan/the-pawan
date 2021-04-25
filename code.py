import json
import difflib
from difflib import get_close_matches
data=json.load(open("data.json"))

word=input("Enter any word :")
word=word.lower()

def word_finder (word):
    if word in data:
        meaning=data[word]
        return meaning
    elif word.title() in data:
        aa=word.title()
        return data[aa]
    elif word.upper() in data:
        bb=word.upper()
        return data[bb]
    elif len(get_close_matches(word,data.keys()))>0:
        inp=input(" did you mean [{}] instead! if yes press y, if no press n :- ".format(get_close_matches(word,data.keys())[0]))
        if inp == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif inp=="n":
            return "word does not exist! please double check it."
        else:
            return "Invalid entry!"
    else:
        return "word does not exist !"

final=(word_finder(word))
if isinstance(final,list):
    for i in final:
        print(i)
else:
    print(final)
