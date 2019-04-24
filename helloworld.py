import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(u"you are someone trying to get free labor")
for token in doc:
        print(token.text, token.pos_, token.dep_)


doc2 = nlp(u"That is a really nice Github")
for token in doc2:
        print(token.text, token.pos_, token.dep_)
