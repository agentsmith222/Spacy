import spacy
import string


patterns = []
nlp = spacy.load("en_core_web_sm")
str = u"That is a really nice Github. Do you need help?"
paragraph = str.split(".")

for sentence in paragraph:
    parse = ""
    for token in nlp(sentence):
        # token.text is the word
        # no need to analyze spaces
        if token.pos_ != "SPACE":
            parse = parse + " " + token.pos_ + " " + token.dep_
    patterns.append(parse.strip())

print(patterns)
