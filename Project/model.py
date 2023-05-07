from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
def training():
    
    train = [
        ('I love this sandwich.', 'pos'),
        ('This is an amazing place!', 'pos'),
        ('I feel very good about these beers.', 'pos'),
        ('I do not like this restaurant', 'neg'),
        ('I am tired of this stuff.', 'neg'),
        ("I can't deal with this", 'neg'),
        ("My boss is horrible.", "neg"),
        ("We cannot solve problems with the kind of thinking we employed when we came up with them.", "pos"),
        ("Nurses are a unique kind. They have this insatiable need to care for others, which is both their greatest strength and fatal flaw.","pos"),
    ]
    ANALysis = NaiveBayesClassifier(train)
    return ANALysis

