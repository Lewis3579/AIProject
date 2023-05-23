from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

import model


ANALysis=model.training()
with open("GPTinput.txt","r") as fin:
    text = fin.read()
doc = TextBlob(text, classifier = ANALysis)
with open("GPToutput.txt", "w") as fout:
    for sent in doc.sentences:
        fout.write(str(sent))
        fout.write(" (")
        fout.write(str(sent.classify()))
        fout.write(")\n")

