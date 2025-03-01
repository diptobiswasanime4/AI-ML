import spacy

nlp = spacy.blank("en")

doc = nlp("Everybody in the king's court was shocked to hear it. Such a big sentence for such a small crime!")

for token in doc:
    print(token)