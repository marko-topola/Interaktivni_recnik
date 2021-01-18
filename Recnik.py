import json
from difflib import get_close_matches

data = json.load(open("data.json"))

word = input("Enter your word: ")
while word != 'EXIT':

    def getDefinition(word):
        word = word.lower()
        if word in data:
            return data[word]
        elif len(get_close_matches(word,data.keys())) > 0:
            close_match = get_close_matches(word, data.keys())[0]
            print("Did you mean "+ close_match +" instead? Enter Y if yes or N if no: " )

            choice = input()
            choice = choice.lower()
            if choice == 'y':
                return data[close_match],
            elif choice == 'n':
                return 'The word does not exist. Please change it a bit or try another word.'
            else:
                'Wrong entry. Try with y or n'
        else:
            return "Your word does not exist. Please check and try again."

    definition = getDefinition(word)
    if type(definition) == list:
        for item in definition:
            print(item)
    else:
        print(definition)

    word = input("Enter your word: ")
