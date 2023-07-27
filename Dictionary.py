import json
from difflib import get_close_matches
data=json.load(open('C:/Users/USER/JSON file/data.json',encoding='utf-8'))
def  translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title in data:
        return data[word.title()]
    elif word.upper in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        print("Oops! did you mean %s instead" %get_close_matches(word,data.keys())[0])
        result=input("Press Y/N:")
        if result=="Y":
            return
        data[get_close_matches(word,data.keys())[0]]
    elif  result=="N":
            return("Oops ! Wrong one :/")
        
    
word=input("Enter Your Word: ")
output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
    else:
        print(output)        
