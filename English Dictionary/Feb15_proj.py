import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def lookup(userinput):
    userinput = userinput.lower()
    if userinput in data:
        return data[userinput]
    elif userinput.upper() in data:
        return data[userinput.upper()]
    elif userinput.title() in data:
        return data[userinput.title()]
    elif len(get_close_matches(userinput, data.keys())) > 0:
        cont = input("Did you mean %s instead? Enter Y if yes, N is no" % get_close_matches(userinput, data.keys())[0])
        if cont == "Y":
            return data[get_close_matches(userinput, data.keys())[0]]
        elif cont == "N":
            return "The word doesn't exist."
        else:
            return "We didn't understand."
    else:
        return "The word doesn't exist. Please double check it."

userinput = input("Enter a word:")
output = lookup(userinput)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
