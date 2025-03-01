import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Jack and Joe were eating in a tavern when suddenly they heard a loud noise outside. All the people rushed outside to see what happened. They're patient people, they're still eating, so is the Tavern guy, completely unbothered.")

# print(nlp.pipeline)

for token in doc:
    print(token, " | ", token.pos_ , " | ", token.lemma_)