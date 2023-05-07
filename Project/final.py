from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import model
with open("input.txt","r") as fin:
    text = fin.read()

ANALysis=model.training()
with open("input.txt","r") as fin:
    text = fin.read()
doc = TextBlob(text, classifier = ANALysis)
with open("output.txt", "w") as fout:
    for sent in doc.sentences:
        fout.write(str(sent))
        fout.write(" (")
        fout.write(str(sent.classify()))
        fout.write(")\n")