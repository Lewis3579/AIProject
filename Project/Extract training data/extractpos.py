import spacy
from textblob import TextBlob
nlp = spacy.load("en_core_web_sm")
with open("posin.txt","r") as fin:
    text = fin.read()
text = text.replace("+","")
text = text.replace("\n"," ")
text = text.replace("'","")
doc = TextBlob(text)

#for sent in doc.sentences:
#    print("('", end='')
#    print(sent, end='')
#    print("', 'neg'),")
with open("posout.txt","w") as fout:
    for sent in doc.sentences:
        fout.write("('")
        fout.write(str(sent))
        fout.write("', 'pos'),\n")
fin.close()
fout.close()
