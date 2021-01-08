import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def translate(w):
    w = w.lower()  # to lower case
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:  # in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " %
                   get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter your desired word to find: ")
output = translate(word)
if type(output) == list:  # for words with two or more meanings we have to display them sequentially not in lists
    for item in output:
        print(item)
else:  # but for every other outputs like prompt or error its ok to just print them
    print(output)
