import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(u"Like you're someone trying to get free labor")
for token in doc:
        print(token.text, token.pos_, token.dep_)
