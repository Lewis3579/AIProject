import spacy
from spacy.matcher import Matcher
nlp = spacy.load("en_core_web_md")
with open("GPTinput.txt","r") as fin:
    text = fin.read()
with open("Humaninput.txt","r") as fin2:
    humanText = fin2.read()
matcher = Matcher(nlp.vocab)
pattern = [{"POS":"PROPN", "OP":"+"},{"POS":"VERB"},{"POS":"ADJ"}]
matcher.add("PROPER_NOUN", [pattern], greedy = "LONGEST")
doc2 = nlp(humanText)
doc3 = nlp(text)
matches = matcher(doc2)
matches.sort(key = lambda x: x[1])
for match in matches[0:]:
    print(match,doc2[match[1]:match[2]])
with open("Humanoutput.txt","w") as fout2:
    for ent in list(doc2.ents):
        fout2.write(str(ent.text))
        fout2.write(" ")
        fout2.write(str(ent.label_))
        fout2.write("\n")
    fout2.write("END OF ENTITY SEARCHING")
    for match in matches[0:]:
        fout2.write(str(match))
        fout2.write(" ")
        fout2.write(str(doc2[match[1]:match[2]]))
        fout2.write("\n")
print("The similarity between text by GPT and human is: ",doc3.similarity(doc2))