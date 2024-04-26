def revsentence(sentence):
    words=sentence.split()
    revwords=words[::-1]
    revsentence=" ".join(revwords)
    return revsentence
sentence=input("enter")
revsentence=revsentence(sentence)
print("revered",revsentence)