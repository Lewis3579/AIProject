import spacy
from textblob import TextBlob
nlp = spacy.load("en_core_web_sm")
with open("negin.txt","r") as fin:
    text = fin.read()
text = text.replace("+","")
text = text.replace("\n"," ")
text = text.replace("'","")
doc = TextBlob(text)
fin.close()
#for sent in doc.sentences:
#    print("('", end='')
#    print(sent, end='')
#    print("', 'neg'),")
with open("negout.txt","w") as fout:
    for sent in doc.sentences:
        fout.write("('")
        fout.write(str(sent))
        fout.write("', 'neg'),\n")
fout.close()