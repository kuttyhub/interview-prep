from collections import Counter
def generateDocument(characters, document):
    # Write your code here.
    if document == "":
        return True

    cdic = dict(Counter(characters))
    ddic = dict(Counter(document))
    print(cdic)
    print(ddic)
    for k,v in ddic.items():
        if cdic.get(k) is None or cdic[k] < v:
            return False

    return True


characters= "Bste!hetsi ogEAxpelrt x "
document="AlgoExpert is the Best!"
# characters="A"
# document= "a"
# characters= "a hsgalhsa sanbjksbdkjba kjx"
# document=""
# characters= "helloworld "
# document="hello wOrld"

print(generateDocument(characters,document))